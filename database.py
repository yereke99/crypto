from sqlite3 import connect
from dbQuery import*

class Database():
    def __init__(self):
        self.db = connect("crypto.db")
        self.cursor = self.db.cursor()
        self.createTable = """
                           CREATE TABLE crypto(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_user INTEGER,
                                usdt INTEGER 
                            )
                           """

        self.insertData = """
                            INSERT INTO crypto(
                                id_user,
                                usdt
                            )VALUES(?,?)  
                          """                   
        self.fetch_ = """Select id_user FROM crypto"""

    def createDB(self):
        self.cursor.execute(self.createTable)
        print("Created table")

    def insertDB(self, id_user: int, usdt: int):
        self.cursor.execute(self.insertData, (id_user, usdt, ))
        self.db.commit()

    def fetch(self) -> list:
        self.cursor.execute(self.fetch_)
        res = self.cursor.fetchall()
        s = []
        for r in res:
            for i in r:
                s.append(i)

        return s

    def gather(self):
        self.cursor.execute("Select id_user From crypto")
        idx = []
        for id in self.cursor.fetchall():
            s = int(''.join(map(str, id)))
            idx.append(s)

        return idx    
    
    def check(self, id_user: int):
        list_of_id = self.gather()

        if id_user in list_of_id:
            return True
        
        return False
    
    def delete(self, id_user: int):
        self.cursor.execute("Delete From crypto WHERE id_user=?", (id_user, ))
        self.db.commit()

if __name__ == "__main__":
    db = Database()
    #db.createDB()
    print(db.fetch())