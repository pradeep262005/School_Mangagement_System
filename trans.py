from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel,showinfo,WARNING
from bus import Database
import sqlite3

root = Tk()
trans = Database("trans.db")
root.title("Amrita Vidyalayam Tirupur")
root.geometry("768x1366+0+0")
root.config(bg="gold")
root.state("zoomed")


name = StringVar()
clas = StringVar()
bus= StringVar()
route= StringVar()
picking= StringVar()
dro= StringVar()
dist= IntVar()
rate= IntVar()
mon= IntVar()
tpri= StringVar()
search_by=StringVar()
search_txt=StringVar()
search_by1=StringVar()
search_txt1=StringVar()




photo = PhotoImage(file = r"H:\School\img\amrits.png")
photoimage = photo.subsample(6,6)

photo1=PhotoImage(file = r"H:\School\img\bus.png")
photoimage1=photo1.subsample(3,3)

  


entries_frame = Frame(root, bg="#54596d")
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Amrita Vidyalayam Tirupur",font=("Comic Sans MS",32, "bold"), bg="#54596d", fg="lavender blush",image=photoimage,compound=RIGHT)
title.grid(row=0, columnspan=3, padx=10, pady=10, sticky="w")
title = Label(entries_frame, text="Transport", font=("Comic Sans MS",20, "bold"), bg="#54596d", fg="lavender blush",image=photoimage1,compound=RIGHT)
title.grid(row=1, columnspan=3, padx=10, pady=10, sticky="w")


lblName = Label(entries_frame, text="Name", font=("Forte", 16), bg="#54596d", fg="black")
lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 16), width=20)
txtName.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblclas = Label(entries_frame, text="Class", font=("Forte", 16), bg="#54596d", fg="black")
lblclas.grid(row=2, column=2, padx=10, pady=10, sticky="w")
comboclas= ttk.Combobox(entries_frame, font=("Corbel", 16), width=18, textvariable=clas, state="readonly")
comboclas['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
comboclas.grid(row=2, column=3, padx=10, sticky="w")

lblbus = Label(entries_frame, text="Bus No", font=("Forte", 16), bg="#54596d", fg="black")
lblbus.grid(row=3, column=0, padx=10, pady=10, sticky="w")
combobus= ttk.Combobox(entries_frame, font=("Corbel", 16), width=18, textvariable=bus, state="readonly")
combobus['values'] = (1,2,3,4,5,6,7,8,9,10,)
combobus.grid(row=3, column=1, padx=10, sticky="w")

lblrou= Label(entries_frame, text="Route", font=("Forte", 16), bg="#54596d", fg="black")
lblrou.grid(row=3, column=2, padx=10, pady=10, sticky="w")
txtrou = Entry(entries_frame, textvariable=route, font=("Corbel", 16), width=20)
txtrou.grid(row=3, column=3, padx=10, pady=10, sticky="w")



lblpic= Label(entries_frame, text="Picking Point", font=("Forte", 16), bg="#54596d", fg="black")
lblpic.grid(row=3, column=4, padx=10, pady=10, sticky="w")
txtpic= Entry(entries_frame, textvariable=picking, font=("Corbel", 16), width=20)
txtpic.grid(row=3, column=5, padx=10, pady=10, sticky="w")

lbldp= Label(entries_frame, text="Dropping Point", font=("Forte", 16), bg="#54596d", fg="black")
lbldp.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtdp= Entry(entries_frame, textvariable=dro, font=("Corbel", 16), width=20)
txtdp.grid(row=4, column=1, padx=10, pady=10, sticky="w")

lbldist= Label(entries_frame, text="Distance", font=("Forte", 16), bg="#54596d", fg="black")
lbldist.grid(row=4, column=2, padx=10, pady=10, sticky="w")
txtdist= Entry(entries_frame, textvariable=dist, font=("Corbel", 16), width=20)
txtdist.grid(row=4, column=3, padx=10, pady=10, sticky="w")

lblrat= Label(entries_frame, text="Rate", font=("Forte", 16), bg="#54596d", fg="black")
lblrat.grid(row=4, column=4, padx=10, pady=10, sticky="w")
txtrat= Entry(entries_frame, textvariable=rate, font=("Corbel", 16), width=20)
txtrat.grid(row=4, column=5, padx=10, pady=10, sticky="w")

lblmon= Label(entries_frame, text="Months Travelled", font=("Forte", 16), bg="#54596d", fg="black")
lblmon.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtmon= Entry(entries_frame, textvariable=mon, font=("Corbel", 16), width=20)
txtmon.grid(row=5, column=1, padx=10, pady=10, sticky="w")

lblpri= Label(entries_frame, text="TOTAL FEES", font=("Forte", 16), bg="#54596d", fg="black")
lblpri.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txtpri= Entry(entries_frame, textvariable=tpri, font=("Corbel", 16), width=20)
txtpri.grid(row=6, column=1, padx=10, pady=10, sticky="w")

detailframe=Frame(root,bd=4,relief=RIDGE,bg='#54596d')
detailframe.place(x=0,y=680,width=1980,height=80)
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
combosearch1['values'] = ("BusNo")
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
    bus.set(row[3])
    route.set(row[4])
    picking.set(row[5])
    dro.set(row[6])
    dist.set(row[7])
    rate.set(row[8])
    mon.set(row[9])
    tpri.set([row[10]])
   
    
    

def dispalyAll():
    tv.delete(*tv.get_children())
    for row in trans.fetch():
        tv.insert("", END, values=row)
def add_bus():
    if txtName.get() == "" or comboclas.get() == "" or combobus.get() == "" or txtrou.get()  == "" or txtpic.get() == "" or txtdp.get() == "" or txtdist.get() == ""or txtrat.get() == ""or txtmon.get() == ""or txtpri.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All Details")
        return
    trans.insert(txtName.get(),comboclas.get(), combobus.get() ,txtrou.get(),txtpic.get(),txtdp.get(),txtdist.get(),txtrat.get(), txtmon.get(), txtpri.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()

def update_bus():
    if txtName.get() == "" or comboclas.get() == "" or combobus.get() == "" or txtrou.get()  == "" or txtpic.get() == "" or txtdp.get() == "" or txtdist.get() == ""or txtrat.get() == ""or txtmon.get() == ""or txtpri.get()=="":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    trans.update(row[0],txtName.get(),comboclas.get(), combobus.get() ,txtrou.get(),txtpic.get(),txtdp.get(),txtdist.get(),txtrat.get(), txtmon.get(), txtpri.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll()
    dispalyAll()

def delete_bus():
     a=askokcancel(
        title='Confirmation',
        message="Are you sure to delete",
        icon=WARNING)
     if a:
        trans.remove(row[0])
        dispalyAll()
        clearAll()
        showinfo(
            title='Deletion',
            message='Deleted Successfully')

def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('trans.db')
        cursor=conn.execute("SELECT * FROM trans WHERE name LIKE ?", ('%' + str(search_txt.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()
def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('trans.db')
        cursor=conn.execute("SELECT * FROM trans WHERE bus LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()

def total():
    t=int(dist.get() * mon.get () * rate.get())
    tpri.set(t)
   
    

def clearAll():
    name.set("")
    clas.set("")
    bus.set("")
    route.set("")
    picking.set("")
    dro.set("")
    dist.set("")
    rate.set("")
    mon.set("")
    tpri.set("")
    
    

    

btn_frame = Frame(entries_frame, bg="#54596d")
btn_frame.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_bus, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#f39c12", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_bus, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#16a085",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_bus, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#2980b9",
                   bd=0).grid(row=0, column=2, padx=10)
btnTotal = Button(btn_frame, command=total, text="Total Fee", width=15, relief = GROOVE,font=("Calibri", 16, "bold"), fg="white",
                  bg="#c0392b",
                  bd=0).grid(row=0, column=3, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#c0392b",
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
tree_frame.place(x=0, y=460, width=1366, height=240)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro',12),
                rowheight=40)  
style.configure("mystyle.Treeview.Heading", font=('Courier',16))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=5)
tv.heading("2", text="Name")
tv.column("2", width=1)
tv.heading("3", text="Class")
tv.column("3", width=1)
tv.heading("4", text="Bus No")
tv.column("4", width=1)
tv.heading("5", text="Route")
tv.column("5",width=1)
tv.heading("6", text="Picking")
tv.column("6", width=1)
tv.heading("7", text="Drop")
tv.column("7",width=2)
tv.heading("8",text='Distance')
tv.column("8",width=2)
tv.heading("9",text='Rate')
tv.column("9",width=2)
tv.heading("10",text='Month')
tv.column("10",width=2)
tv.heading("11",text='Total Fees')
tv.column("11",width=1)
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
