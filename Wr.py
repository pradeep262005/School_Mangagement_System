from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel, showinfo, WARNING
import sqlite3

# ---------------------------- DATABASE -----------------------------
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS workers(
            id Integer Primary Key,
            name text,
            age text,
            doj text,
            gender text,
            work text,
            contact text,
            aadhar text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, name, age, doj, gender, work, contact, aadhar):
        self.cur.execute("INSERT INTO workers VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                         (name, age, doj, gender, work, contact, aadhar))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM workers")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM workers WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, name, age, doj, gender, work, contact, aadhar):
        self.cur.execute("""
            UPDATE workers SET name=?, age=?, doj=?, gender=?, work=?, contact=?, aadhar=?
            WHERE id=?
        """, (name, age, doj, gender, work, contact, aadhar, id))
        self.con.commit()

# ---------------------------- GUI -----------------------------
db = Database("workers.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1920x1080+0+0")
root.config(bg="gold")
root.state("zoomed")

# Variables
name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
work = StringVar()
contact = StringVar()
aadhar = StringVar()
search_by = StringVar()
search_txt = StringVar()
search_by1 = StringVar()
search_txt1 = StringVar()

# UI Frames
entries_frame = Frame(root, bg="maroon")
entries_frame.pack(side=TOP, fill=X)

# Labels and Inputs
Label(entries_frame, text="Worker's Registration", font=("Georgia", 20, "bold"), bg="maroon", fg="#f39c12").grid(row=0, columnspan=4, padx=10, pady=20, sticky="w")

Label(entries_frame, text="Name", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=30).grid(row=1, column=1, padx=10, pady=10, sticky="w")

Label(entries_frame, text="Age", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=1, column=2, padx=10, pady=10, sticky="w")
Entry(entries_frame, textvariable=age, font=("Corbel", 16), width=30).grid(row=1, column=3, padx=10, pady=10, sticky="w")

Label(entries_frame, text="D.O.B", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=2, column=0, padx=10, pady=10, sticky="w")
Entry(entries_frame, textvariable=doj, font=("Corbel", 16), width=30).grid(row=2, column=1, padx=10, pady=10, sticky="w")

Label(entries_frame, text="Gender", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=2, column=2, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=2, column=3, padx=10, sticky="w")

Label(entries_frame, text="Type of Work", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=3, column=0, padx=10, pady=10, sticky="w")
combowork = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=work, state="readonly")
combowork['values'] = ('Office', 'Driver', 'Cleaners', 'Watchman', 'Gardener', 'Kitchen worker')
combowork.grid(row=3, column=1, padx=10, sticky="w")

Label(entries_frame, text="Contact No", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=3, column=2, padx=10, pady=10, sticky="w")
Entry(entries_frame, textvariable=contact, font=("Corbel", 16), width=30).grid(row=3, column=3, padx=10, sticky="w")

Label(entries_frame, text="Aadhar Number", font=("Segoe UI", 16), bg="maroon", fg="white").grid(row=4, column=0, padx=10, pady=10, sticky="w")
aadhar_entry = Text(entries_frame, width=30, height=1, font=("Corbel", 16))
aadhar_entry.grid(row=4, column=1, padx=10, sticky="w")

# Buttons
btn_frame = Frame(entries_frame, bg="maroon")
btn_frame.grid(row=5, column=0, columnspan=4, padx=10, pady=10, sticky="w")

Button(btn_frame, text="ADD", command=lambda: add_worker(), width=15, font=("Segoe UI", 16, "bold"), bg="#16a085", fg="white").grid(row=0, column=0, padx=5)
Button(btn_frame, text="ALTER", command=lambda: update_worker(), width=15, font=("Segoe UI", 16, "bold"), bg="#2980b9", fg="white").grid(row=0, column=1, padx=5)
Button(btn_frame, text="DELETE", command=lambda: delete_worker(), width=15, font=("Segoe UI", 16, "bold"), bg="#c0392b", fg="white").grid(row=0, column=2, padx=5)
Button(btn_frame, text="CLEAR", command=lambda: clearAll(), width=15, font=("Segoe UI", 16, "bold"), bg="#f39c12", fg="white").grid(row=0, column=3, padx=5)

# Treeview
frame_tree = Frame(root, bg="blue")
frame_tree.place(x=0, y=460, width=1366, height=240)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro', 12), rowheight=40)
style.configure("mystyle.Treeview.Heading", font=('Courier', 18))
tv = ttk.Treeview(frame_tree, columns=(1,2,3,4,5,6,7,8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.heading("2", text="Name")
tv.heading("3", text="Age")
tv.heading("4", text="D.O.B")
tv.heading("5", text="Gender")
tv.heading("6", text="Work")
tv.heading("7", text="Contact No")
tv.heading("8", text="Aadhar")
tv['show'] = 'headings'
tv.pack(fill=X)

# Treeview functions
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[4])
    work.set(row[5])
    contact.set(row[6])
    aadhar_entry.delete(1.0, END)
    aadhar_entry.insert(END, row[7])

tv.bind("<ButtonRelease-1>", getData)

def dispalyAll():
    tv.delete(*tv.get_children())
    for record in db.fetch():
        tv.insert("", END, values=record)

def add_worker():
    if name.get() == "" or age.get() == "" or doj.get() == "" or gender.get() == "" or work.get() == "" or contact.get() == "" or aadhar_entry.get(1.0, END).strip() == "":
        messagebox.showerror("Input Error", "Please Fill All Fields")
        return
    db.insert(name.get(), age.get(), doj.get(), gender.get(), work.get(), contact.get(), aadhar_entry.get(1.0, END).strip())
    messagebox.showinfo("Success", "Record Added")
    clearAll()
    dispalyAll()

def update_worker():
    db.update(row[0], name.get(), age.get(), doj.get(), gender.get(), work.get(), contact.get(), aadhar_entry.get(1.0, END).strip())
    messagebox.showinfo("Success", "Record Updated")
    clearAll()
    dispalyAll()

def delete_worker():
    if askokcancel("Confirm", "Delete this record?", icon=WARNING):
        db.remove(row[0])
        showinfo("Deleted", "Record Deleted")
        clearAll()
        dispalyAll()

def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    work.set("")
    contact.set("")
    aadhar_entry.delete(1.0, END)

# Load data initially
dispalyAll()

root.mainloop()
