from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel,showinfo,WARNING

from me import Database
import sqlite3

me = Database("markss.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1920x1080+0+0")
root.config(bg="gold")
root.state("zoomed")



name = StringVar()
clas = StringVar()
sc=StringVar()
tamil=IntVar()
eng=IntVar()
soc=IntVar()
sb=IntVar()
matb=IntVar()
pa=IntVar()
ce=IntVar()
ip=IntVar()
tText=IntVar()
avgText=StringVar()
search_by=StringVar()
search_txt=StringVar()
search_by1=StringVar()
search_txt1=StringVar()

photo = PhotoImage(file = r"H:\School\img\amrits.png")
photoimage = photo.subsample(6,6)

photo1=PhotoImage(file = r"H:\School\img\mark.png")
photoimage1=photo1.subsample(6,6)

entries_frame = Frame(root, bg="skyblue")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Amrita Vidyalayam Tirupur", font=("Kristen ITC",32, "bold"), bg="skyblue", fg="red",image=photoimage,compound=RIGHT)
title.grid(row=0, columnspan=3, padx=10, pady=20, sticky="w")
title = Label(entries_frame, text="Mark Entry", font=("Kristen ITC",20, "bold"), bg="skyblue", fg="red",image=photoimage1,compound=RIGHT)
title.grid(row=1, columnspan=3, padx=10, pady=20, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Forte", 16), bg="skyblue", fg="black")
lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=20)
txtName.grid(row=2, column=1, padx=10,  sticky="w")

lblclas = Label(entries_frame, text="Class", font=("Forte", 16), bg="skyblue", fg="black")
lblclas.grid(row=2, column=2, padx=8, pady=10, sticky="w")
comboclas= ttk.Combobox(entries_frame, font=("Corbel", 16), width=20, textvariable=clas, state="readonly")
comboclas['values'] = ('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th')
comboclas.grid(row=2, column=3, padx=10, sticky="w")

lblsc = Label(entries_frame, text="Subjects", font=("Forte", 16), bg="skyblue", fg="black")
lblsc.grid(row=2, column=4, padx=10, pady=10, sticky="w")
combosc= ttk.Combobox(entries_frame, font=("Corbel", 16), width=20, textvariable=sc, state="readonly")
combosc['values'] = ('T/E/M/S/SS','E/M/P/C/IP','E/M/P/C/B','E/P/C/B/IP','E/A/Bu/Eco/IP')
combosc.grid(row=2, column=5, padx=10, sticky="w")


lbltamil = Label(entries_frame, text="Tamil", font=("Forte", 16), bg="skyblue", fg="black")
lbltamil.grid(row=3, column=0, padx=10, pady=10, sticky="w")
txttamil= Entry(entries_frame, textvariable=tamil, font=("Corbel", 16), width=20)
txttamil.grid(row=3, column=1, padx=10, pady=10, sticky="w")

lbleng= Label(entries_frame, text="English", font=("Forte", 16), bg="skyblue", fg="black")
lbleng.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txteng = Entry(entries_frame, textvariable=eng, font=("Corbel", 16), width=20)
txteng.grid(row=3, column=3, padx=10, pady=10, sticky="w")



lblsoc= Label(entries_frame, text="Social", font=("Forte", 16), bg="skyblue", fg="black")
lblsoc.grid(row=3, column=4, padx=10, pady=10, sticky="w")
txtsoc= Entry(entries_frame, textvariable=soc, font=("Corbel", 16), width=20)
txtsoc.grid(row=3, column=5, padx=10, pady=10, sticky="w")

lblsb= Label(entries_frame, text="Sci/Bio", font=("Forte", 16), bg="skyblue", fg="black")
lblsb.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtsb= Entry(entries_frame, textvariable=sb, font=("Corbel", 16), width=20)
txtsb.grid(row=4, column=1, padx=10, pady=10, sticky="w")

lblmatb= Label(entries_frame, text="Maths/Bus", font=("Forte", 16), bg="skyblue", fg="black")
lblmatb.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtmatb= Entry(entries_frame, textvariable=matb, font=("Corbel", 16), width=20)
txtmatb.grid(row=4, column=3, padx=10, pady=10, sticky="w")


lblpa= Label(entries_frame, text="Phy/Acc", font=("Forte", 16), bg="skyblue", fg="black")
lblpa.grid(row=4, column=4, padx=10, pady=10, sticky="w")
txtpa= Entry(entries_frame, textvariable=pa, font=("Corbel", 16), width=20)
txtpa.grid(row=4, column=5, padx=10, pady=10, sticky="w")

lblce= Label(entries_frame, text="Che/Eco", font=("Forte", 16), bg="skyblue", fg="black")
lblce.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtce= Entry(entries_frame, textvariable=ce, font=("Corbel", 16), width=20)
txtce.grid(row=5, column=1, padx=10, pady=10, sticky="w")

lblip= Label(entries_frame, text="IP", font=("Forte", 16), bg="skyblue", fg="black")
lblip.grid(row=5, column=2, padx=10, pady=10, sticky="w")
txtip= Entry(entries_frame, textvariable=ip, font=("Corbel", 16), width=20)
txtip.grid(row=5, column=3, padx=10, pady=10, sticky="w")

lbltm= Label(entries_frame, text="TOTAL", font=("Forte", 16), bg="skyblue", fg="black")
lbltm.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txttm= Entry(entries_frame, textvariable=tText, font=("Corbel", 16), width=20)
txttm.grid(row=6, column=1, padx=10, pady=10, sticky="w")

lblav= Label(entries_frame, text="AVG", font=("Forte", 16), bg="skyblue", fg="black")
lblav.grid(row=6, column=2, padx=10, pady=10, sticky="w")
txtav= Entry(entries_frame, textvariable=avgText, font=("Corbel", 16), width=20)
txtav.grid(row=6, column=3, padx=10, pady=10, sticky="w")

detailframe=Frame(root,bd=4,relief=RIDGE,bg='#54596d')
detailframe.place(x=0,y=680,width=1366,height=80)
lblsearch= Label(detailframe, text="Search", font=("Forte", 16), bg="#54596d", fg="white")
lblsearch.grid(row=0, column=0, padx=10, pady=20, sticky="w")
combosearch= ttk.Combobox(detailframe, font=("Corbel", 16), width=15, textvariable=search_by, state="readonly")
combosearch['values'] = ("Name")
combosearch.grid(row=0, column=1, padx=10,pady=20 ,sticky="w")



txtSearch=Entry(detailframe,textvariable=search_txt,width=20,font=("Forte"),bg="pink", fg="blue")
txtSearch.grid(row=0,column=2,pady=20,padx=10,sticky='w')

lblsearch1= Label(detailframe, text="Search", font=("Forte", 16), bg="#54596d", fg="white")
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
    clas.set(row[2])
    sc.set(row[3])
    tamil.set(row[4])
    eng.set(row[5])
    soc.set(row[6])
    sb.set(row[7])
    matb.set(row[8])
    pa.set(row[9])
    ce.set(row[10])
    ip.set(row[11])
    tText.set(row[12])
    avgText.set(row[13])
def dispalyAll():
    tv.delete(*tv.get_children())
    for row in me.fetch():
        tv.insert("", END, values=row)
def add_marks():
    if txtName.get() == "" or comboclas.get() == "" or combosc.get()=="" or txttamil.get() == "" or txteng.get()  == "" or txtsoc.get() == "" or txtsb.get() == "" or txtmatb.get() == ""or txtpa.get() == ""or txtce.get() == ""or txtip.get()==""or txttm.get() == ""or txtav.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Marks")
        return
    me.insert(txtName.get(),comboclas.get(),combosc.get(), txttamil.get() ,txteng.get(),txtsoc.get(),txtsb.get(),txtmatb.get(),txtpa.get(), txtce.get(), txtip.get(),txttm.get(),txtav.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()
def update_marks():
    if txtName.get() == "" or comboclas.get() == "" or combosc.get()=="" or txttamil.get() == "" or txteng.get()  == "" or txtsoc.get() == "" or txtsb.get() == "" or txtmatb.get() == ""or txtpa.get() == ""or txtce.get() == ""or txtip.get()==""or txttm.get() == ""or txtav.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    me.update(row[0],txtName.get(),comboclas.get(),combosc.get(), txttamil.get() ,txteng.get(),txtsoc.get(),txtsb.get(),txtmatb.get(),txtpa.get(), txtce.get(), txtip.get(),txttm.get(),txtav.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll() 

    dispalyAll()
def delete_marks():
     a=askokcancel(
        title='Confirmation',
        message="Are you sure to delete",
        icon=WARNING)
     if a:
        me.remove(row[0])
        clearAll()
        dispalyAll()
        showinfo(
            title='Deletion',
            message='Deleted Successfully')

def total():
    t=int(tamil.get()+eng.get()+soc.get()+sb.get()+matb.get()+pa.get()+ce.get()+ip.get())
    tText.set(t)

    avg=t/5
    avgText.set(avg)
    
    

    if(avg>33):
        showinfo(
            title='Pass',
            message='Well Done')
    else:
       showinfo(
            title='Fail',
            message='Work Hard')

def clearAll():
    name.set("")
    clas.set("")
    sc.set("")
    tamil.set("")
    eng.set("")
    soc.set("")
    sb.set("")
    matb.set("")
    pa.set("")
    ce.set("")
    ip.set("")
    tText.set("")
    avgText.set("")

def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('markss.db')
        cursor=conn.execute("SELECT * FROM markss WHERE name LIKE ?", ('%' + str(search_txt.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()
def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('markss.db')
        cursor=conn.execute("SELECT * FROM markss WHERE clas LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()


    

btn_frame = Frame(entries_frame, bg="skyblue")
btn_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_marks, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#f39c12", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_marks, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#16a085",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_marks, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#2980b9",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)
btnTotal = Button(btn_frame, command=total, text="Total", width=15, relief = GROOVE,font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=4, padx=10)
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord)
searchbtn.grid(row=0, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=4, padx=10,pady=20 ,sticky="w")
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord1)
searchbtn.grid(row=0, column=8, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=9, padx=10,pady=20 ,sticky="w")


tree_frame = Frame(root)
tree_frame.place(x=0, y=490, width=1366, height=190)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro',12),
                rowheight=40)  
style.configure("mystyle.Treeview.Heading", font=('Courier',12))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.column("2", width=1)
tv.heading("3", text="Class")
tv.column("3", width=1)
tv.heading("4", text="Subject")
tv.column("4", width=1)
tv.heading("5", text="Tamil")
tv.column("5",width=1)
tv.heading("6", text="Eng")
tv.column("6", width=1)
tv.heading("7", text="Soc")
tv.column("7",width=2)
tv.heading("8",text='Sci/Bio')
tv.column("8",width=2)
tv.heading("9",text='Mat/Bus')
tv.column("9",width=2)
tv.heading("10",text='Phy/Acc')
tv.column("10",width=2)
tv.heading("11",text='Che/Eco')
tv.column("11",width=1)
tv.heading("12",text='IP')
tv.column("12",width=1)
tv.heading("13",text='Total')
tv.column("13",width=1)
tv.heading("14",text='Average')
tv.column("14",width=2)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
