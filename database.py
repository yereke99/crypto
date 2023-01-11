from sqlite3 import connect
from dbQuery import*

class Database():
    def __init__(self):
        self.db = connect("crypto.db")
        self.cursor = self.db.cursor()