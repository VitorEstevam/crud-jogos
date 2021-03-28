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

    def sel_categoria(self, id):
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'SELECT c.descricao FROM "jogo-categoria" AS jc, categoria AS c where jc."idJogo" = {id} AND c.id = jc."idCategoria"')
            _connect.commit()

            response = _cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return response

    def sel_mecanica(self, id):
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'SELECT m.descricao FROM  "jogo-mecanica"  AS jm, mecanica AS m where jm."idJogo" = {id} AND m.id = jm."idMecanica"')
            _connect.commit()

            response = _cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return response

    def sel_designer(self, id):
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f'SELECT d.nome FROM  "jogo-designer"  AS jd, designer AS d where jd."id_jogo" = {id} AND d.id = jd."id_designer"')
            _connect.commit()

            response = _cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            return "an error occurred"

        else:
            return response

    def sel_all_attributes_from_jogo(self, id):
        a = {}
        a["designers"] = self.sel_designer(id)
        a["categoria"] = self.sel_categoria(id)
        a["mecanica"] = self.sel_mecanica(id)
        return a

    def select_from_db(self, id):  # read single
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            a = f'SELECT * FROM (SELECT jogo.*, tipo.descricao AS tipo FROM jogo INNER JOIN Tipo ON jogo.idtipo=tipo.id WHERE jogo.id={id}) AS j'
            _cursor.execute(a)
            _connect.commit()
            response = _cursor.fetchone()
            response.update(self.sel_all_attributes_from_jogo(id))

        except (Exception, psycopg2.Error) as error:
            if(_connect):
                _cursor.close()
                _connect.close()
            return "an error occurred"

        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        return json.dumps(response)

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
