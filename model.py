import sys

import psycopg2

from config import DATABASE


class Model:
    def __init__(self):
        self.connection = None
        self.connect()
        self.cur = self.connection.cursor()

    def connect(self):
        try:
            self.connection = psycopg2.connect(database=DATABASE["DATABASE"], user=DATABASE["USER"],
                                               password=DATABASE["PASSWORD"])
        except psycopg2.DatabaseError as e:
            print('Error %s' % e)
            sys.exit(1)
        print("Connected")

    def close(self):
        self.connection.close()

    def drop_table(self):
        self.cur.execute("drop table theuser")
        self.connection.commit()

    def create_table(self):
        self.cur.execute("CREATE TABLE theuser (id serial PRIMARY KEY, name varchar(50), email varchar(50), age integer)")
        self.connection.commit()

    def insert(self, user):
        self.cur.execute("insert into theuser (name, email, age) values ('%s', '%s', '%d')" %
                         (user['name'], user['email'], user['age']))

    def select_all(self):
        self.cur.execute('select * from theuser')
        return self.cur.fetchall()
