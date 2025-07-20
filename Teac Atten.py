import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING

# ---------- DATABASE CLASS ----------
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS tea(
            id Integer Primary Key,
            name text,
            sub text,
            mon text,
            year text,
            present int,
            abse int
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, sub, mon, year, present, abse):
        self.cur.execute("insert into tea values (NULL,?,?,?,?,?,?)",
                         (name, sub, mon, year, present, abse))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from tea")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from tea where id=?", (id,))
        self.con.commit()

    def update(self, id, name, sub, mon, year, present, abse):
        self.cur.execute(
            "update tea set name=?, sub=?,mon=?,year=?, present=?, abse=? where id=?",
            (name, sub, mon, year, present, abse, id))
        self.con.commit()


ta = Database("tea.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1920x1080+0+0")
root.config(bg="gold")
root.state("zoomed")

name = StringVar()
sub = StringVar()
mon = StringVar()
year = StringVar()
present = IntVar()
abse = IntVar()
search_by = StringVar()
search_txt = StringVar()
search_by1 = StringVar()
search_txt1 = StringVar()

photo = PhotoImage(file=r"H:\School\img\amrits.png")
photoimage = photo.subsample(4, 4)

photo1 = PhotoImage(file=r"H:\School\img\att.png")
photoimage1 = photo1.subsample(3, 3)

photo2 = PhotoImage(file=r"H:\School\img\amma.png")
photoimage2 = photo2.subsample(4, 4)

entries_frame = Frame(root, bg="cyan")
entries_frame.place(x=0, y=0, width=720, height=768)

title = Label(entries_frame, text="Amrita Vidyalayam Tirupur", font=("Jokerman", 32, "bold"),
              bg="cyan", fg="crimson", image=photoimage, compound=RIGHT)
title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
title = Label(entries_frame, text="ATTENDANCE", font=("Jokerman", 20, "bold"),
              bg="cyan", fg="crimson", image=photoimage1, compound=RIGHT)
title.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Forte", 16), bg="cyan", fg="crimson")
lblName.grid(row=3, column=0, padx=10, pady=20, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=30)
txtName.grid(row=3, column=1, padx=10, pady=20, sticky="w")

lblsub = Label(entries_frame, text="Suject", font=("Forte", 16), bg="cyan", fg="crimson")
lblsub.grid(row=4, column=0, padx=10, pady=10, sticky="w")
combosub = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=sub, state="readonly")
combosub['values'] = ('Tamil', 'English', 'Maths', 'Science', 'Social', 'CS', 'IP', 'ARTS', 'Others')
combosub.grid(row=4, column=1, padx=10, sticky="w")

lblmon = Label(entries_frame, text="Month", font=("Forte", 16), bg="cyan", fg="crimson")
lblmon.grid(row=5, column=0, padx=10, pady=20, sticky="w")
combomon = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=mon, state="readonly")
combomon['values'] = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC")
combomon.grid(row=5, column=1, padx=10, pady=20, sticky="w")

lblyear = Label(entries_frame, text="YEAR", font=("Forte", 16), bg="cyan", fg="crimson")
lblyear.grid(row=6, column=0, padx=10, pady=20, sticky="w")
txtyear = Entry(entries_frame, textvariable=year, font=("Corbel", 16), width=30)
txtyear.grid(row=6, column=1, padx=10, pady=20, sticky="w")

lblpres = Label(entries_frame, text="No.of Days Present", font=("Forte", 16), bg="cyan", fg="crimson")
lblpres.grid(row=7, column=0, padx=10, pady=20, sticky="w")
txtpres = Entry(entries_frame, textvariable=present, font=("Corbel", 16), width=30)
txtpres.grid(row=7, column=1, padx=10, pady=20, sticky="w")

lblabse = Label(entries_frame, text="No.of Days Absent", font=("Forte", 16), bg="cyan", fg="crimson")
lblabse.grid(row=8, column=0, padx=10, pady=20, sticky="w")
txtabse = Entry(entries_frame, textvariable=abse, font=("Corbel", 16), width=30)
txtabse.grid(row=8, column=1, padx=10, pady=20, sticky="w")

detailframe = Frame(root, bd=4, relief=RIDGE, bg='crimson')
detailframe.place(x=720, y=0, width=645, height=150)

lblsearch = Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="gold")
lblsearch.grid(row=0, column=0, padx=10, pady=20, sticky="w")
combosearch = ttk.Combobox(detailframe, font=("Corbel", 16), width=10, textvariable=search_by, state="readonly")
combosearch['values'] = ("Subject",)
combosearch.grid(row=0, column=1, padx=10, pady=20, sticky="w")

lblsearch1 = Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="gold")
lblsearch1.grid(row=1, column=0, padx=10, pady=20, sticky="w")
combosearch1 = ttk.Combobox(detailframe, font=("Corbel", 16), width=10, textvariable=search_by1, state="readonly")
combosearch1['values'] = ("Month",)
combosearch1.grid(row=1, column=1, padx=10, pady=20, sticky="w")

txtSearch = Entry(detailframe, textvariable=search_txt, width=20, font=("Forte"), bg="pink", fg="blue")
txtSearch.grid(row=0, column=2, pady=10, padx=20, sticky='w')
txtSearch1 = Entry(detailframe, textvariable=search_txt1, width=20, font=("Forte"), bg="pink", fg="blue")
txtSearch1.grid(row=1, column=2, pady=10, padx=20, sticky='w')

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    sub.set(row[2])
    mon.set(row[3])
    year.set(row[4])
    present.set(row[5])
    abse.set(row[6])

def add_att():
    if txtName.get() == "" or combosub.get() == "" or combomon.get() == "" or txtyear.get() == "" or present.get() == "" or txtabse.get() == "":
        messagebox.showerror("Erorr in Input", "Fill the Attendance")
        return
    ta.insert(txtName.get(), combosub.get(), combomon.get(), txtyear.get(), present.get(), txtabse.get())
    messagebox.showinfo("Success", "Marked Attendance")
    clearAll()
    dispalyAll()

def update_att():
    if txtName.get() == "" or combosub.get() == "" or combomon.get() == "" or txtyear.get() == "" or present.get() == "" or txtabse.get() == "":
        messagebox.showerror("Erorr in Input", "Fill the Attendance")
        return
    ta.update(row[0], txtName.get(), combosub.get(), combomon.get(), txtyear.get(), present.get(), txtabse.get())
    messagebox.showinfo("Success", "Attendance Updated")
    clearAll()
    dispalyAll()

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in ta.fetch():
        tv.insert("", END, values=row)

def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('tea.db')
        cursor = conn.execute("SELECT * FROM tea WHERE sub LIKE ?", ('%' + str(search_txt.get()) + '%',))
        for row in cursor.fetchall():
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()

def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('tea.db')
        cursor = conn.execute("SELECT * FROM tea WHERE mon LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        for row in cursor.fetchall():
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()

def delete_att():
    a = askokcancel(title='Confirmation', message="Are you sure to delete", icon=WARNING)
    if a:
        ta.remove(row[0])
        clearAll()
        dispalyAll()
        showinfo(title='Deletion', message='Deleted Successfully')

def clearAll():
    name.set("")
    sub.set("")
    mon.set("")
    year.set("")
    present.set("")
    abse.set("")

btn_frame = Frame(entries_frame, bg="cyan")
btn_frame.grid(row=9, column=0, columnspan=4, padx=10, pady=40, sticky="w")

Button(btn_frame, command=add_att, text="Mark Attendance", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#16a085", bd=0).grid(row=0, column=0)
Button(btn_frame, command=update_att, text="Update Attendance", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#2980b9", bd=0).grid(row=0, column=1, padx=10)
Button(btn_frame, command=delete_att, text="Delete Attendance", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#c0392b", bd=0).grid(row=0, column=2, padx=10)
Button(btn_frame, command=clearAll, text="Clear All", width=15, font=("Calibri", 16, "bold"), fg="white",
       bg="#f39c12", bd=0).grid(row=0, column=3, padx=10)

Button(detailframe, text="Search", width=10, pady=5, command=SearchRecord).grid(row=0, column=3, padx=10, pady=20)
Button(detailframe, text="Show All", width=10, pady=5, command=dispalyAll).grid(row=0, column=4, padx=10, pady=20)
Button(detailframe, text="Search", width=10, pady=5, command=SearchRecord1).grid(row=1, column=3, padx=10, pady=20)
Button(detailframe, text="Show All", width=10, pady=5, command=dispalyAll).grid(row=1, column=4, padx=10, pady=20)

entries_frame = Frame(root, bg="crimson")
entries_frame.place(x=720, y=550, width=645, height=260)

Label(entries_frame, text="The main purpose of education \n should be to impart \n a culture of the heart. \n - AMMA",
      font=("forte", 26, "bold"), bg="crimson", fg="gold", image=photoimage2, compound=RIGHT).grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

tree_frame = Frame(root)
tree_frame.place(x=720, y=150, width=645, height=400)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro', 12), rowheight=40)
style.configure("mystyle.Treeview.Heading", font=('Forte', 16))
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="S.NO")
tv.heading("2", text="Name")
tv.heading("3", text="Subject")
tv.heading("4", text="Month")
tv.heading("5", text="Year")
tv.heading("6", text="Present")
tv.heading("7", text=" Absent")
tv.column("1", width=2)
tv.column("2", width=6)
tv.column("3", width=5)
tv.column("4", width=2)
tv.column("5", width=5)
tv.column("6", width=5)
tv.column("7", width=15)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
