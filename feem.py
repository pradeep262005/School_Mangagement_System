from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askokcancel,showinfo,WARNING

from feedb import Database
import sqlite3

feedb = Database("fee.db")
root = Tk()
root.title("Amrita Vidyalayam Tirupur")
root.geometry("1366x768+0+0")
root.config(bg="gold")
root.state("zoomed")



name = StringVar()
clas = StringVar()
ftotal=IntVar()
fpaid=IntVar()
ftpay=IntVar()
dtotal=IntVar()
dpaid=IntVar()
dtpay=IntVar()
totalfeep=IntVar()
totalfeet=IntVar()
search_by=StringVar()
search_txt=StringVar()
search_by1=StringVar()
search_txt1=StringVar()

photo = PhotoImage(file = r"H:\School\img\amrits.png")
photoimage = photo.subsample(6,6)

photo1=PhotoImage(file = r"H:\School\img\mark.png")
photoimage1=photo1.subsample(6,6)


photo2 = PhotoImage(file = r"H:\School\img\amma.png")
photoimage2 = photo2.subsample(4,4)


entries_frame = Frame(root, bg="purple3")
entries_frame.place(x=0,y=0,width=720,height=768)
title = Label(entries_frame, text="Amrita Vidyalayam Tirupur", font=("Kristen ITC",28, "bold"), bg="purple3", fg="gold",image=photoimage,compound=RIGHT)
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
title = Label(entries_frame, text="FEE", font=("Kristen ITC",24, "bold"), bg="purple3", fg="gold",image=photoimage1,compound=RIGHT)
title.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

lblName = Label(entries_frame, text="Name", font=("Forte", 18), bg="purple3", fg="black")
lblName.grid(row=2, column=0, padx=10, pady=10, sticky="w")
txtName = Entry(entries_frame, textvariable=name, font=("Corbel", 12), width=25)
txtName.grid(row=2, column=1, padx=10, pady=10, sticky="w")

lblclas = Label(entries_frame, text="Class", font=("Forte", 18), bg="purple3", fg="black")
lblclas.grid(row=3, column=0, padx=10, pady=10, sticky="w")
comboclas= ttk.Combobox(entries_frame, font=("Corbel", 12), width=23, textvariable=clas, state="readonly")
comboclas['values'] = ('1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th')
comboclas.grid(row=3, column=1, padx=10, sticky="w")


lblftotal = Label(entries_frame, text="Total Fees", font=("Forte", 18), bg="purple3", fg="black")
lblftotal.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtftotal= Entry(entries_frame, textvariable=ftotal, font=("Corbel", 12), width=25)
txtftotal.grid(row=4, column=1, padx=10, pady=10, sticky="w")

lblfpaid= Label(entries_frame, text="Fees Paid", font=("Forte",18), bg="purple3", fg="black")
lblfpaid.grid(row=5, column=0, padx=10, pady=10, sticky="w")
txtfpaid= Entry(entries_frame, textvariable=fpaid, font=("Corbel", 12), width=25)
txtfpaid.grid(row=5, column=1, padx=10, pady=10, sticky="w")



lblftpay= Label(entries_frame, text="Fees to be paid", font=("Forte", 18), bg="purple3", fg="black")
lblftpay.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txtftpay= Entry(entries_frame, textvariable=ftpay, font=("Corbel", 12), width=25)
txtftpay.grid(row=6, column=1, padx=10, pady=10, sticky="w")

lbldtotal= Label(entries_frame, text="Total Due Amount", font=("Forte", 18), bg="purple3", fg="black")
lbldtotal.grid(row=7, column=0, padx=10, pady=10, sticky="w")
txtdtotal= Entry(entries_frame, textvariable=dtotal, font=("Corbel", 12), width=25)
txtdtotal.grid(row=7, column=1, padx=10, pady=10, sticky="w")

lbldpaid= Label(entries_frame, text="Due Paid", font=("Forte", 18), bg="purple3", fg="black")
lbldpaid.grid(row=8, column=0, padx=10, pady=10, sticky="w")
txtdpaid= Entry(entries_frame, textvariable=dpaid, font=("Corbel", 12), width=25)
txtdpaid.grid(row=8, column=1, padx=10, pady=10, sticky="w")


lbldtpay= Label(entries_frame, text="Due to pay", font=("Forte",18), bg="purple3", fg="black")
lbldtpay.grid(row=9, column=0, padx=10, pady=10, sticky="w")
txtdtpay= Entry(entries_frame, textvariable=dtpay, font=("Corbel", 12), width=25)
txtdtpay.grid(row=9, column=1, padx=10, pady=10, sticky="w")

lbltotalfeep= Label(entries_frame, text="Total Amount Paid", font=("Forte", 18), bg="purple3", fg="black")
lbltotalfeep.grid(row=10, column=0, padx=10, pady=10, sticky="w")
txttotalfeep= Entry(entries_frame, textvariable=totalfeep, font=("Corbel", 12), width=25)
txttotalfeep.grid(row=10, column=1, padx=10, pady=10, sticky="w")

lbltotalfeet= Label(entries_frame, text="Total Amount to be paid", font=("Forte", 18), bg="purple3", fg="black")
lbltotalfeet.grid(row=11, column=0, padx=10, pady=10, sticky="w")
txttotalfeet= Entry(entries_frame, textvariable=totalfeet, font=("Corbel", 12), width=25)
txttotalfeet.grid(row=11, column=1, padx=10, pady=10, sticky="w")


detailframe=Frame(root,bd=4,relief=RIDGE,bg='purple1')
detailframe.place(x=700,y=0,width=670,height=150)
lblsearch= Label(detailframe, text="Search", font=("Forte", 18), bg="purple1", fg="white")
lblsearch.grid(row=0, column=0, padx=10, pady=20, sticky="w")
combosearch= ttk.Combobox(detailframe, font=("Corbel", 12), width=12, textvariable=search_by, state="readonly")
combosearch['values'] = ("Name")
combosearch.grid(row=0, column=1, padx=10,pady=20 ,sticky="w")



txtSearch=Entry(detailframe,textvariable=search_txt,width=12,font=("Forte"),bg="pink", fg="blue")
txtSearch.grid(row=0,column=2,pady=20,padx=10,sticky='w')

lblsearch1= Label(detailframe, text="Search", font=("Forte", 18), bg="purple1", fg="white")
lblsearch1.grid(row=1, column=0, padx=10, pady=20, sticky="w")
combosearch1= ttk.Combobox(detailframe, font=("Corbel", 16), width=12, textvariable=search_by1, state="readonly")
combosearch1['values'] = ("Class")
combosearch1.grid(row=1, column=1, padx=10,pady=20 ,sticky="w")

txtSearch1=Entry(detailframe,textvariable=search_txt1,width=12,font=("Forte"),bg="pink", fg="blue")
txtSearch1.grid(row=1,column=2,pady=10,padx=20,sticky='w')



def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    clas.set(row[2])
    ftotal.set(row[3])
    fpaid.set(row[4])
    ftpay.set(row[5])
    dtotal.set(row[6])
    dpaid.set(row[7])
    dtpay.set(row[8])
    totalfeep.set(row[9])
    totalfeet.set(row[10])
def dispalyAll():
    tv.delete(*tv.get_children())
    for row in feedb.fetch():
        tv.insert("", END, values=row)
def add_marks():
    if txtName.get() == "" or comboclas.get() == "" or txtftotal.get() == "" or txtfpaid.get()  == "" or txtftpay.get() == "" or txtdtotal.get() == "" or txtdpaid.get() == ""or txtdtpay.get() == ""or txttotalfeep.get() == ""or txttotalfeet.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Marks")
        return
    feedb.insert(txtName.get(),comboclas.get(),txtftotal.get() ,txtfpaid.get(),txtftpay.get(),txtdtotal.get(),txtdpaid.get(),txtdtpay.get(), txttotalfeep.get(),txttotalfeet.get())
    messagebox.showinfo("Success", "Record Inserted")
    clearAll()
    dispalyAll()
def update_marks():
    if txtName.get() == "" or comboclas.get() == "" or txtftotal.get() == "" or txtfpaid.get()  == "" or txtftpay.get() == "" or txtdtotal.get() == "" or txtdpaid.get() == ""or txtdtpay.get() == ""or txttotalfeep.get() == ""or txttotalfeet.get() == "":
        messagebox.showerror("Erorr in Input", "Please Fill All the Details")
        return
    feedb.update(row[0],txtName.get(),comboclas.get(),txtftotal.get() ,txtfpaid.get(),txtftpay.get(),txtdtotal.get(),txtdpaid.get(),txtdtpay.get(), txttotalfeep.get(),txttotalfeet.get())
    messagebox.showinfo("Success", "Record Update")
    clearAll() 

    dispalyAll()
def delete_marks():
     a=askokcancel(
        title='Confirmation',
        message="Are you sure to delete",
        icon=WARNING)
     if a:
        feedb.remove(row[0])
        clearAll()
        dispalyAll()
        showinfo(
            title='Deletion',
            message='Deleted Successfully')


def total():
    t=int(ftotal.get()-fpaid.get())
    ftpay.set(t)

    r=int(dtotal.get()-dpaid.get())
    dtpay.set(r)

    c=int(fpaid.get()+dpaid.get())
    totalfeep.set(c)

    a=int(ftotal.get()+dtotal.get()-fpaid.get()+dpaid.get())
    totalfeet.set(a)

   
def clearAll():
    name.set("")
    clas.set("")
    ftotal.set("")
    fpaid.set("")
    ftpay.set("")
    dtotal.set("")
    dpaid.set("")
    dtpay.set("")
    totalfeep.set("")
    totalfeet.set("")

def SearchRecord():
    if search_txt.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('fee.db')
        cursor=conn.execute("SELECT * FROM fee WHERE name LIKE ?", ('%' + str(search_txt.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()
def SearchRecord1():
    if search_txt1.get() != "":
        tv.delete(*tv.get_children())
        conn = sqlite3.connect('fee.db')
        cursor=conn.execute("SELECT * FROM fee WHERE clas LIKE ?", ('%' + str(search_txt1.get()) + '%',))
        fetch = cursor.fetchall()
        for row in fetch:
            tv.insert('', 'end', values=row)
        cursor.close()
        conn.close()


    

btn_frame = Frame(entries_frame, bg="purple3")
btn_frame.grid(row=12, column=0, columnspan=4, padx=10, pady=10, sticky="w")
btnAdd = Button(btn_frame, command=add_marks, text="Add ", width=10, font=("Calibri", 16, "bold"), fg="white",
                bg="#f39c12", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=update_marks, text="Update ", width=10, font=("Calibri", 16, "bold"),
                 fg="white", bg="#16a085",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=delete_marks, text="Delete ", width=10, font=("Calibri", 16, "bold"),
                   fg="white", bg="#2980b9",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clearAll, text="Clear ", width=10, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)
btnTotal = Button(btn_frame, command=total, text="Total", width=10, relief = GROOVE,font=("Calibri", 16, "bold"), fg="white",
                  bg="green",
                  bd=0).grid(row=0, column=4, padx=10)
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord)
searchbtn.grid(row=0, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=0, column=4, padx=10,pady=20 ,sticky="w")
searchbtn=Button(detailframe,text="Search",width=10,pady=5,command=SearchRecord1)
searchbtn.grid(row=1, column=3, padx=10,pady=20 ,sticky="w")
showallbtn=Button(detailframe,text="Show All",width=10,pady=5,command=dispalyAll)
showallbtn.grid(row=1, column=4, padx=10,pady=20 ,sticky="w")
entries_frame = Frame(root, bg="purple1")
entries_frame.place(x=700,y=550,width=670,height=260)

title = Label(entries_frame, text="Spiritual education is a training\n that helps us to truly undertstand ourselves \n - AMMA", font=("Calibri",20, "bold"), bg="purple1", fg="lawngreen",image=photoimage2,compound=RIGHT)
title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")

tree_frame = Frame(root)
tree_frame.place(x=700, y=150, width=670, height=400)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Trajan Pro',12),
                rowheight=40)  
style.configure("mystyle.Treeview.Heading", font=('Courier',14))  
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7,8,9,10,11), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width=1)
tv.heading("2", text="Name")
tv.column("2", width=4)
tv.heading("3", text="Class")
tv.column("3", width=1)
tv.heading("4", text="Fee")
tv.column("4",width=3)
tv.heading("5", text="PaidFee")
tv.column("5", width=3)
tv.heading("6", text="Topay")
tv.column("6",width=3)
tv.heading("7",text='Due')
tv.column("7",width=3)
tv.heading("8",text='PaidDue')
tv.column("8",width=3)
tv.heading("9",text='Duetopay')
tv.column("9",width=3)
tv.heading("10",text='TotalPaid')
tv.column("10",width=3)
tv.heading("11",text='Amttopay')
tv.column("11",width=3)

tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

dispalyAll()
root.mainloop()
