import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS fee(
            id Integer Primary Key,
            name text,
            clas text,
            ftotal int,
            fpaid int,
            ftpay int,
            dtotal int,
            dpaid int,
            dtpay int,
            totalfeep int,
            totalfeet int
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name,clas,ftotal,fpaid,ftpay,dtotal,dpaid,dtpay,totalfeep,totalfeet):
        self.cur.execute("insert into fee values(NULL,?,?,?,?,?,?,?,?,?,?)",
                         ( name,clas,ftotal,fpaid,ftpay,dtotal,dpaid,dtpay,totalfeep,totalfeet))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from fee order by clas")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from fee where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id,name,clas,ftotal,fpaid,ftpay,dtotal,dpaid,dtpay,totalfeep,totalfeet):
        self.cur.execute("update fee set name=?, clas=?,ftotal=?, fpaid=?, ftpay=?, dtotal=?, dpaid=?,dtpay=? ,totalfeep=?,totalfeet=? where id=?",
            ( name,clas,ftotal,fpaid,ftpay,dtotal,dpaid,dtpay,totalfeep,totalfeet, id))
        self.con.commit()
