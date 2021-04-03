from connections.connection import DAO
import psycopg2
from psycopg2.extras import RealDictCursor
import json


class MecanicaDAO(DAO):

    def insert_on_db(self, desc):  # create
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f"INSERT INTO mecanica(descricao) VALUES ('{desc}');")
            _cursor.execute(
                f"SELECT id FROM mecanica WHERE id = (SELECT max(id) FROM mecanica)")
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

        return json.dumps(response[0], indent=2)

    def select_from_db(self, id):  # read single
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(
                f"select * from mecanica where id = {str(id)}")
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

        return json.dumps(response, indent=2)

    def select_all_from_db(self):  # read all
        results = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(f"select * from mecanica")
            _connect.commit()

            response = _cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            if(_connect):
                _cursor.close()
                _connect.close()
            return "an error occurred"

        finally:
            if(_connect):
                _cursor.close()
                _connect.close()

        return json.dumps(response, indent=2)

    def update_on_db(self, id, desc):  # update
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f"UPDATE mecanica set descricao='{desc}' WHERE id={str(id)};")
            _cursor.execute(f'SELECT * FROM mecanica where id = {str(id)}')
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
        return json.dumps(response[0], indent=2)

    def remove_from_db(self, id):  # delete
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(f"DELETE FROM mecanica WHERE id = {str(id)}")
            _cursor.execute(f'SELECT * FROM mecanica where id = {str(id)}')
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
