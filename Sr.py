from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel,showinfo,WARNING
from db import Database
import sqlite3

db = Database("students.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1920x1080+0+0")
root.config(bg="gold")
root.state("zoomed")

name = StringVar()
age = StringVar()
doj = StringVar()
gender = StringVar()
clas = StringVar()
contact = StringVar()
aadhar=StringVar()
search_by=StringVar()
search_txt=StringVar()
search_by1=StringVar()
search_txt1=StringVar()


photo = PhotoImage(file = r"H:\School\img\amrits.png")
photoimage = photo.subsample(6,6)

photo1=PhotoImage(file = r"H:\School\img\student.png")
photoimage1=photo1.subsample(6,6)

entries_frame = Frame(root, bg="green")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Amrita Vidyalayam Tirupur", font=("Kristen ITC",32, "bold"), bg="green", fg="gold",image=photoimage,compound=RIGHT)
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
title = Label(entries_frame, text="Student's Registartion", font=("Kristen ITC",20, "bold"), bg="green", fg="gold",image=photoimage1,compound=RIGHT)
title.grid(row=1, columnspan=2, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Forte", 16), bg="green", fg="white")
lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=30)
txtName.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblAge = Label(entries_frame, text="Age", font=("Forte", 16), bg="green", fg="white")
lblAge.grid(row=2, column=2, padx=10, pady=10, sticky="w")
txtAge = Entry(entries_frame, textvariable=age, font=("Corbel", 16), width=30)
txtAge.grid(row=2, column=3, padx=10, pady=10, sticky="w")

lbldoj = Label(entries_frame, text="D.O.B", font=("Forte", 16), bg="green", fg="white")
lbldoj.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txtDoj = Entry(entries_frame, textvariable=doj, font=("Corbel", 16), width=30)
txtDoj.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lblclas = Label(entries_frame, text="Class", font=("Forte", 16), bg="green", fg="white")
lblclas.grid(row=3, column=2, padx=10, pady=10, sticky="w")
comboclas= ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=clas, state="readonly")
comboclas['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
comboclas.grid(row=3, column=3, padx=10, sticky="w")

lblGender = Label(entries_frame, text="Gender", font=("Forte", 16), bg="green", fg="white")
lblGender.grid(row=4, column=0, padx=10, pady=10, sticky="w")
comboGender = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female")
comboGender.grid(row=4, column=1, padx=10, sticky="w")

lblContact = Label(entries_frame, text="Contact No", font=("Forte", 16), bg="green", fg="white")
lblContact.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtContact = Entry(entries_frame, textvariable=contact, font=("Corbel", 16), width=30)
txtContact.grid(row=4, column=3, padx=10, sticky="w")

lblaadhar = Label(entries_frame, text="AadharNumber", font=("Forte", 16), bg="green", fg="white")
lblaadhar.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtaadhar = Text(entries_frame, width=30,height=1,font=("Corbel", 16))
txtaadhar.grid(row=5, column=1, padx=10, sticky="w")


detailframe=Frame(root,bd=4,relief=RIDGE,bg='crimson')
detailframe.place(x=0,y=690,width=1366,height=80)
lblsearch= Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="white")
lblsearch.grid(row=0, column=0, padx=10, pady=20, sticky="w")
combosearch= ttk.Combobox(detailframe, font=("Corbel", 16), width=15, textvariable=search_by, state="readonly")
combosearch['values'] = ("Aadhar")
combosearch.grid(row=0, column=1, padx=10,pady=20 ,sticky="w")



txtSearch=Entry(detailframe,textvariable=search_txt,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch.grid(row=0,column=2,pady=20,padx=10,sticky='w')

lblsearch1= Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="white")
lblsearch1.grid(row=0, column=5, padx=10, pady=20, sticky="w")
combosearch1= ttk.Combobox(detailframe, font=("Corbel", 16), width=15, textvariable=search_by1, state="readonly")
combosearch1['values'] = ("Class")
combosearch1.grid(row=0, column=6, padx=10,pady=20 ,sticky="w")

txtSearch1=Entry(detailframe,textvariable=search_txt1,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch1.grid(row=0,column=7,pady=10,padx=20,sticky='w')




def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    clas.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtaadhar.delete(1.0, END)
    txtaadhar.insert(END, row[7])

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)


def add_students():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or comboclas.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtaadhar.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.insert(txtName.get(),txtAge.get(), txtDoj.get() , comboclas.get() ,comboGender.get(), txtContact.get(), txtaadhar.get(
            1.0, END))
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()



def update_students():
    if txtName.get() == "" or txtAge.get() == "" or txtDoj.get() == "" or comboclas.get() == "" or comboGender.get() == "" or txtContact.get() == "" or txtaadhar.get(
            1.0, END) == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDoj.get(),comboclas.get(), comboGender.get(), txtContact.get(),
              txtaadhar.get(
                  1.0, END))
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()


def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('students.db')
        cursor=conn.execute("SELECT * FROM students WHERE aadhar LIKE ?", ('%' + str(search_txt.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()
def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('students.db')
        cursor=conn.execute("SELECT * FROM students WHERE clas LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()


                                  
    
    
    

def delete_students():
     a=askokcancel(
        title='Confirmation',
        message="Are you sure to delete",
        icon=WARNING)
     if a:
        db.remove(row[0])
        clearAll()
        dispalyAll()
        showinfo(
            title='Deletion',
            message='Deleted Successfully')

        
def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    clas.set("")
    contact.set("")
    txtaadhar.delete(1.0, END)
    

btn_frame = Frame(entries_frame, bg="green")
btn_frame.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_students, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_students, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_students, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord)
searchbtn.grid(row=0, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=4, padx=10,pady=20 ,sticky="w")
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord1)
searchbtn.grid(row=0, column=8, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=9, padx=10,pady=20 ,sticky="w")



tree_frame = Frame(root, bg="pink")
tree_frame.place(x=0, y=460, width=1366, height=250)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro',12),
                rowheight=40)  
style.configure("mystyle.Treeview.Heading", font=('Courier',18))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7,8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.column("2",width=5)
tv.heading("3", text="Age")
tv.column("3", width=5)
tv.heading("4", text="D.O.B")
tv.column("4", width=5)
tv.heading("5", text="Class")
tv.column("5",width=5)
tv.heading("6", text="Gender")
tv.column("6", width=5)
tv.heading("7", text="Contact")
tv.column("7",width=5)
tv.heading("8",text="Aadhar")
tv.column("8",width=5)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
