from connections.connection import DAO
import psycopg2
from psycopg2.extras import RealDictCursor
import json


class CategoriaDAO(DAO):

    def insert_on_db(self, desc):  # create
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f"INSERT INTO categoria(descricao) VALUES ('{desc}');")
            _cursor.execute(
                f"SELECT id FROM categoria WHERE id = (SELECT max(id) FROM categoria)")
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

        return json.dumps(response[0])

    def select_from_db(self, id):  # read single
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(
                f"select * from categoria where id = {str(id)}")
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

        return json.dumps(response)

    def select_all_from_db(self):  # read all
        results = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor(cursor_factory=RealDictCursor)
            _cursor.execute(f"select * from categoria")
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

        return json.dumps(response)

    def update_on_db(self, id, desc):  # update
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f"UPDATE categoria set descricao='{desc}' WHERE id={str(id)};")
            _cursor.execute(f'SELECT * FROM categoria where id = {str(id)}')
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
        return json.dumps(response[0])

    def remove_from_db(self, id):  # delete
        response = ''
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(f"DELETE FROM categoria WHERE id = {str(id)}")
            _cursor.execute(f'SELECT * FROM categoria where id = {str(id)}')
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
