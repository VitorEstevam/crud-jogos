from connections.connection import DAO
import psycopg2
from psycopg2.extras import RealDictCursor
import json


class DesignerDAO(DAO):

    def insert_on_db(self, name):  # create
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(f"INSERT INTO designer(nome)VALUES ('{name}');")
            _cursor.execute(
                f"SELECT id FROM Designer WHERE id = (SELECT max(id) FROM designer)")
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
                f"select id,nome from designer where id = {str(id)}")
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
            _cursor.execute(f"select id,nome from designer")
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

    def update_on_db(self, id, nome):  # update
        response = []
        try:
            _connect = self._initialize_connection()
            _cursor = _connect.cursor()
            _cursor.execute(
                f"UPDATE designer set nome='{nome}' WHERE id={str(id)};")
            _cursor.execute(f'SELECT * FROM designer where id = {str(id)}')
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
            _cursor.execute(f"DELETE FROM designer WHERE id = {str(id)}")
            _cursor.execute(f'SELECT * FROM designer where id = {str(id)}')
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
