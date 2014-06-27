import sqlite3
import phonebook as pb

class DB(object):
    def __init__(self):
        self.conn = sqlite3.connect('phonebook.db')
        self.cursor = self.conn.cursor()

class Phonebook(pb.Phonebook):
    def __init__(self, db):
        self.db = db
        query = '''select * from entries'''
        res = self.db.cursor.execute(query)
        self.entries = dict((name, pb.Entry(name, num)) for name, num in res.fetchall())

    def add(self, name, number):
        add_query = '''insert into entries values (?, ?)'''
        to_print = super(Phonebook, self).add(name, number)
        with self.db.conn:
            self.db.conn.execute(add_query, (name, number))
        return to_print

    def change(self, name, number):
        change_query = '''update entries set number = ? where name = ?'''
        to_print = super(Phonebook, self).change(name, number)
        with self.db.conn:
            self.db.conn.execute(change_query, (name, number))
        return to_print

    def remove(self, name):
        remove_query = '''delete from entries where name = ?'''
        to_print = super(Phonebook, self).remove(name)
        with self.db.conn:
            self.db.conn.execute(remove_query, (name))
        return to_print
