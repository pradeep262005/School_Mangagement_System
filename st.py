import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS stu(
            id Integer Primary Key,
            name text,
            clas text,
            mon text,
            year text,
            present int,
            abse int
            
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, clas,mon,year,present,abse):
        self.cur.execute("insert into stu values (NULL,?,?,?,?,?,?)"
                         ,(name, clas,mon,year,present,abse))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from stu")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from stu where id=?", (id,))
        self.con.commit()

       
        
  # Update a Record in DB
    def update(self,id, name, clas,mon,year,present,abse):
        self.cur.execute(
            "update stu set name=?, clas=?,mon=?,year=?, present=?, abse=? where id=?",
            (name, clas,mon,year,present,abse,id))
        self.con.commit()


    
