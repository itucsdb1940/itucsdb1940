import os
import psycopg2 as db


class Client(object):

    def __init__(self):
        self.dsn = os.getenv('DATABASE_URL')
        self.connection = db.connect(self.dsn)
        self.cursor = self.connection.cursor()

    def query(self, statement, params=None):
        try:
            self.cursor.execute(statement, params)
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

    def fetch(self, statement, params=None):
        try:
            self.cursor.execute(statement, params)
            self.connection.commit()
            return self.cursor.fetchall()
        except:
            self.connection.rollback()
            raise

    def create(self, statement, params=None):
        try:
            self.cursor.execute(statement, params)
            self.connection.commit()
        except Exception as err:
            self.connection.rollback()
            return '{}'.format(err)

    def __del__(self):
        self.connection.close()
        self.cursor.close()


db_client = Client()
