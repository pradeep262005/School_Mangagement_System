import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS markss(
            id Integer Primary Key,
            name text,
            clas text,
            sc text,
            tamil int,
            eng int,
            soc int,
            sb int,
            matb int,
            pa int,
            ce int,
            ip int,
            tText int,
            avgText text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name,clas,sc,tamil,eng,soc,sb,matb,pa,ce,ip,tText,avgText):
        self.cur.execute("insert into markss values(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         ( name,clas,sc,tamil,eng,soc,sb,matb,pa,ce,ip,tText,avgText))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from markss order by clas")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from markss where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id,name,clas,sc,tamil,eng,soc,sb,matb,pa,ce,ip,tText,avgText):
        self.cur.execute("update markss set name=?, clas=?,sc=?, tamil=?, eng=?, soc=?, sb=?, matb=? ,pa=?,ce=?,ip=?,tText=?,avgText=? where id=?",
            ( name,clas,sc,tamil,eng,soc,sb,matb,pa,ce,ip,tText,avgText, id))
        self.con.commit()
