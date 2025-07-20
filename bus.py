import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS trans(
            id Integer Primary Key,
            name text,
            clas text,
            bus text,
            route text,
            picking text,
            dro text,
            dist int,
            rate int,
            mon int,
            pri text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name,clas,bus,route,picking,dro,dist,rate,mon,pri):
        self.cur.execute("insert into trans values(NULL,?,?,?,?,?,?,?,?,?,?)",
                         (name,clas,bus,route,picking,dro,dist,rate,mon,pri))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from trans")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from trans where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id,name,clas,bus,route,picking,dro,dist,rate,mon,pri):
        self.cur.execute(
            "update trans set name=?, clas=?, bus=?, route=?,picking=?,dro=?,dist=?,rate=?,mon=?,pri=? where id=?",
            ( name,clas,bus,route,picking,dro,dist,rate,mon,pri,id))
        self.con.commit()
