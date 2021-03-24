import psycopg2
import abc


class DAO():
    data = {
        'host': 'localhost',
        'database': 'jogosney',
        'user': 'postgres',
        'password': '123456'
    }

    def _initialize_connection(self):
        _connect = psycopg2.connect(
            host=self.data['host'],
            database=self.data['database'],
            user=self.data['user'],
            password=self.data['password'])
        return _connect
