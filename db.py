import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS students(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            clas text,
            gender text,
            contact text,
            aadhar text unique
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, doj, clas, gender, contact, aadhar):
        self.cur.execute("insert into students values (NULL,?,?,?,?,?,?,?)",
                         (name, age, doj, clas, gender, contact, aadhar))
        self.con.commit()

    # Fetch All Data from DB
    def fetch(self):
        self.cur.execute("SELECT * from students")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from students where id=?", (id,))
        self.con.commit() 

   
        
  # Update a Record in DB
    def update(self, id, name, age, doj,clas, gender, contact, aadhar):
        self.cur.execute(
            "update students set name=?, age=?, doj=?, clas=?, gender=?, contact=?, aadhar=? where id=?",
            (name, age, doj, clas, gender, contact, aadhar, id))
        self.con.commit()


    
