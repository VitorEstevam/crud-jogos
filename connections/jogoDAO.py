from connections.connection import DAO
import psycopg2
from psycopg2.extras import RealDictCursor
import json


class JogoDAO(DAO):

    def insert_on_db(self, idade, nome, tempo, jogadoresMin, jogadoresMax, idTipo):  # create
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            a = f"INSERT INTO jogo(idade, nome, tempo, jogadoresmin, jogadoresmax, idtipo) VALUES({idade}, '{nome}', {tempo}, {jogadoresMin}, {jogadoresMax}, {idTipo})"
            _cursor.execute(a)
            _cursor.execute(
                'select id from jogo where id=(SELECT max(id) FROM jogo)')
            _connect.commit()
            response = _cursor.fetchone()

            id = json.dumps(response[0])
            # for i in categorias:
            #     self.add_categoria(id, i)
            # for i in designers:
            #     self.add_designer(id, i)
            # for i in mecanicas:
            #     self.add_mecanica(id, i)

        except (Exception, psycopg2.Error) as error:
            if(_connect):
                _cursor.close()
                _connect.close()
            return "an error occurred"

        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        return id

    def remove_from_db(self, id):  # delete
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'DELETE FROM "jogo-mecanica" WHERE "idJogo" = {str(id)}')
            _cursor.execute(
                f'DELETE FROM "jogo-categoria" WHERE "idJogo" = {str(id)}')
            _cursor.execute(
                f'DELETE FROM "jogo-designer" WHERE "id_jogo" = {str(id)}')
            _cursor.execute(
                f'DELETE FROM jogo WHERE id = {str(id)}')
            _cursor.execute(
                f'Select * from jogo WHERE id = {str(id)}')
            _connect.commit()
            response = _cursor.fetchone()

        except (Exception, psycopg2.Error) as error:
            if(_connect):
                _cursor.close()
                _connect.close()

            return "an error occurred"
        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        if(response == None):
            return 'deleted'

    def add_categoria(self, idJogo, idCategoria):
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'INSERT INTO "jogo-categoria"("idJogo", "idCategoria") VALUES({idJogo}, {idCategoria})')
            _connect.commit()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return "success"

    def add_mecanica(self, idJogo, idMecanica):
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'INSERT INTO "jogo-mecanica"("idJogo", "idMecanica") VALUES({idJogo}, {idMecanica})')
            _connect.commit()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return "success"

    def add_designer(self, idJogo, idDesigner):
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'INSERT INTO "jogo-designer"("id_jogo", "id_designer") VALUES({idJogo}, {idDesigner})')
            _connect.commit()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return "success"

           # def select_from_db(self, id):  # read single
           #     response = ''
           #     try:
           #         _connect = self._initialize_connection()
           #         _cursor = _connect.cursor(cursor_factory=RealDictCursor)
           #         _cursor.execute(
           #             f"select * from tipo where id = {str(id)}")
           #         _connect.commit()
           #         response = _cursor.fetchone()

           #     except (Exception, psycopg2.Error) as error:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()
           #         return "an error occurred"

           #     finally:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()

           #     return json.dumps(response)

           # def select_all_from_db(self):  # read all
           #     results = []
           #     try:
           #         _connect = self._initialize_connection()
           #         _cursor = _connect.cursor(cursor_factory=RealDictCursor)
           #         _cursor.execute(f"select * from tipo")
           #         _connect.commit()

           #         response = _cursor.fetchall()

           #     except (Exception, psycopg2.Error) as error:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()
           #         return "an error occurred"

           #     finally:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()

           #     return json.dumps(response)

           # def update_on_db(self, id, desc):  # update
           #     response = []
           #     try:
           #         _connect = self._initialize_connection()
           #         _cursor = _connect.cursor()
           #         _cursor.execute(
           #             f"UPDATE tipo set descricao='{desc}' WHERE id={str(id)};")
           #         _cursor.execute(f'SELECT * FROM tipo where id = {str(id)}')
           #         _connect.commit()
           #         response = _cursor.fetchone()

           #     except (Exception, psycopg2.Error) as error:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()
           #         return "an error occurred"

           #     finally:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()
           #     return json.dumps(response[0])

           # def remove_from_db(self, id):  # delete
           #     response = ''
           #     try:
           #         _connect = self._initialize_connection()
           #         _cursor = _connect.cursor()
           #         _cursor.execute(f"DELETE FROM tipo WHERE id = {str(id)}")
           #         _cursor.execute(f'SELECT * FROM tipo where id = {str(id)}')
           #         _connect.commit()
           #         response = _cursor.fetchone()

           #     except (Exception, psycopg2.Error) as error:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()

           #         return "an error occurred"
           #     finally:
           #         if(_connect):
           #             _cursor.close()
           #             _connect.close()

           #     if(response == None):
           #         return 'deleted'
