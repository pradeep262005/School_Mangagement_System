from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel,showinfo,WARNING
from st import Database
import sqlite3

st= Database("stu.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1920x1080+0+0")
root.config(bg="gold")
root.state("zoomed")

name = StringVar()
clas = StringVar()
mon = StringVar()
year= StringVar()
present=IntVar()
abse= IntVar()
search_by=StringVar()
search_txt=StringVar()
search_by1=StringVar()
search_txt1=StringVar()

photo = PhotoImage(file = r"H:\School\img\amrits.png")
photoimage = photo.subsample(4,4)

photo1=PhotoImage(file = r"H:\School\img\att.png")
photoimage1=photo1.subsample(3,3)

photo2 = PhotoImage(file = r"H:\School\img\amma.png")
photoimage2 = photo2.subsample(4,4)

entries_frame = Frame(root, bg="pink")
entries_frame.place(x=0,y=0,width=720,height=768)

title = Label(entries_frame, text="Amrita Vidyalayam Tirupur", font=("Kristen ITC",30, "bold"), bg="pink", fg="blue",image=photoimage,compound=RIGHT)
title.grid(row=0, columnspan=3, padx=10, pady=10, sticky="w")
title = Label(entries_frame, text="ATTENDANCE", font=("Kristen ITC",18, "bold"), bg="pink", fg="blue",image=photoimage1,compound=RIGHT)
title.grid(row=1, columnspan=3, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Forte", 16), bg="pink", fg="blue")
lblName.grid(row=3, column=0, padx=10, pady=20, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=30)
txtName.grid(row=3, column=1, padx=10, pady=20, sticky="w")

lblclas = Label(entries_frame, text="Class", font=("Forte", 16), bg="pink", fg="blue")
lblclas.grid(row=4, column=0, padx=10, pady=20, sticky="w")
comboclas= ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=clas, state="readonly")
comboclas['values'] = ('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th')
comboclas.grid(row=4, column=1, padx=10,pady=20, sticky="w")

lblmon= Label(entries_frame, text="Month", font=("Forte", 16), bg="pink", fg="blue")
lblmon.grid(row=5, column=0, padx=10, pady=20, sticky="w")
combomon = ttk.Combobox(entries_frame, font=("Corbel", 16), width=28, textvariable=mon, state="readonly")
combomon['values'] = ("JAN", "FEB","MAR","APR","MAY","JUN","JUL","AUG","SEPT","OCT","NOV","DEC")
combomon.grid(row=5, column=1, padx=10,pady=20 ,sticky="w")

lblyear = Label(entries_frame, text="YEAR", font=("Forte", 16), bg="pink", fg="blue")
lblyear.grid(row=6, column=0, padx=10, pady=20, sticky="w")
txtyear = Entry(entries_frame, textvariable=year, font=("Corbel", 16), width=30)
txtyear.grid(row=6, column=1, padx=10, pady=20, sticky="w")

lblpres = Label(entries_frame, text="No.of Days Present", font=("Forte", 16), bg="pink", fg="blue")
lblpres.grid(row=7, column=0, padx=10, pady=20, sticky="w")
txtpres = Entry(entries_frame, textvariable=present, font=("Corbel", 16), width=30)
txtpres.grid(row=7, column=1, padx=10, pady=20, sticky="w")







lblabse = Label(entries_frame, text="No.of Days Absent", font=("Forte", 16), bg="pink", fg="blue")
lblabse.grid(row=8, column=0, padx=10, pady=20, sticky="w")
txtabse = Entry(entries_frame, textvariable=abse, font=("Corbel", 16), width=30)
txtabse.grid(row=8, column=1, padx=10, pady=20, sticky="w")



        
detailframe=Frame(root,bd=4,relief=RIDGE,bg='crimson')
detailframe.place(x=720,y=0,width=645,height=150)
lblsearch= Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="blue")
lblsearch.grid(row=0, column=0, padx=10, pady=20, sticky="w")
combosearch= ttk.Combobox(detailframe, font=("Corbel", 16), width=10, textvariable=search_by, state="readonly")
combosearch['values'] = ("Class")
combosearch.grid(row=0, column=1, padx=10,pady=20 ,sticky="w")
lblsearch1= Label(detailframe, text="Search", font=("Forte", 16), bg="crimson", fg="blue")
lblsearch1.grid(row=1, column=0, padx=10, pady=20, sticky="w")
combosearch1= ttk.Combobox(detailframe, font=("Corbel", 16), width=10, textvariable=search_by1, state="readonly")
combosearch1['values'] = ("Month")
combosearch1.grid(row=1, column=1, padx=10,pady=20 ,sticky="w")


txtSearch=Entry(detailframe,textvariable=search_txt,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch.grid(row=0,column=2,pady=10,padx=20,sticky='w')
txtSearch=Entry(detailframe,textvariable=search_txt,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch.grid(row=0,column=2,pady=10,padx=20,sticky='w')

txtSearch1=Entry(detailframe,textvariable=search_txt1,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch1.grid(row=1,column=2,pady=10,padx=20,sticky='w')
txtSearch1=Entry(detailframe,textvariable=search_txt1,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch1.grid(row=1,column=2,pady=10,padx=20,sticky='w')








def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    clas.set(row[2])
    mon.set(row[3])
    year.set(row[4])
    present.set(row[5])
    abse.set(row[6])




def add_att():
    if txtName.get() == "" or comboclas.get() == "" or combomon.get() == "" or txtyear.get()==""  or present.get() == "" or txtabse.get() == "":
        messagebox.showerror("Erorr in Input", "Fill the Attendance")
        return
    st.insert(txtName.get(),comboclas.get(),combomon.get() ,txtyear.get(),present.get() , txtabse.get())
    messagebox.showinfo("Success", "Marked Attendance")
    clearAll()
    dispalyAll()



def update_att():
    if  txtName.get() == "" or comboclas.get() == "" or combomon.get() == "" or txtyear.get()==""  or present.get() == "" or txtabse.get() == "":
        messagebox.showerror("Erorr in Input", "Fill the Attendance")
        return
    st.update(row[0],txtName.get(),comboclas.get(),combomon.get() ,txtyear.get(),present.get() , txtabse.get())
    messagebox.showinfo("Success", "Attendance Updated")
    clearAll()
    dispalyAll()


def dispalyAll():
    tv.delete(*tv.get_children())
    for row in st.fetch():
        tv.insert("", END, values=row)

def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('stu.db')
        cursor=conn.execute("SELECT * FROM stu WHERE clas  LIKE? ", ('%' + str(search_txt.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()
def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('stu.db')
        cursor=conn.execute("SELECT * FROM stu WHERE mon LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()



                                  
    
    
    

def delete_att():
     a=askokcancel(
        title='Confirmation',
        message="Are you sure to delete",
        icon=WARNING)
     if a:
        st.remove(row[0])
        clearAll()
        dispalyAll()
        showinfo(
            title='Deletion',
            message='Deleted Successfully')

        
def clearAll():
    name.set("")
    clas.set("")
    mon.set("")
    year.set("")
    present.set("")
    abse.set("")


def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    clas.set(row[2])
    mon.set(row[3])
    year.set(row[4])
    present.set(row[5])
    abse.set(row[6])
    
btn_frame = Frame(entries_frame, bg="pink")
btn_frame.grid(row=9, column=0, columnspan=4, padx=10, pady=40, sticky="w")
btnAdd = Button(btn_frame, command=add_att, text="Mark Attendance", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_att, text="Update Attendance", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_att, text="Delete Attendance", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear All", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)

searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord)
searchbtn.grid(row=0, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=4, padx=10,pady=20 ,sticky="w")
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord1)
searchbtn.grid(row=1, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=1, column=4, padx=10,pady=20 ,sticky="w")

entries_frame = Frame(root, bg="gold")
entries_frame.place(x=720,y=550,width=645,height=260)

title = Label(entries_frame, text="Go out and serve the suffering.\n Learn to place others in front of yourself \n - AMMA", font=("Calibri",22, "bold"), bg="gold", fg="blue",image=photoimage2,compound=RIGHT)
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")


tree_frame = Frame(root)
tree_frame.place(x=720, y=150, width=645, height=400)


style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro',12),
                rowheight=40)
style.configure("mystyle.Treeview.Heading", font=('Forte',18))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7), style="mystyle.Treeview")
tv.heading("1", text="S.NO")
tv.column("1", width=2)
tv.heading("2", text="Name")
tv.column("2",width=6)
tv.heading("3", text="Class")
tv.column("3", width=5)
tv.heading("4", text="Month")
tv.column("4", width=2)
tv.heading("5", text="Year")
tv.column("5",width=5)
tv.heading("6", text="Present")
tv.column("6", width=5)
tv.heading("7", text=" Absent")
tv.column("7",width=15)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
