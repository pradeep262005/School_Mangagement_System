import pygame
from subprocess import call
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from itertools import cycle
import PIL.Image
from time import strftime
import datetime as dt


try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_stureg():
    call(["python", "Sr.py"])
def click_teareg():
    call(["python", "Tr.py"])
def click_workreg():
    call(["python", "Wr.py"])
def click_stuatt():
    call(["python","Stu Atten.py"])
def click_teaatt():
    call(["python","Teac Atten.py"])
def click_clasatt():
    call(["python","atten classwise.py"])
def click_mark():
    call(["python","marks.py"])
def click_clas12():
    call(["python","12th.py"])
def click_clas10():
    call(["python","10th.pyw"])
def click_claswise():
    call(["python","classwise.py"])
def click_fee():
    call(["python","feem.py"])
def click_trans():
    call(["python","trans.py"])



class Avt:
    def __init__(self):

        

        root = Tk()
        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#ffffff' # X11 color: 'white'
        _ana1color = '#ffffff' # X11 color: 'white'
        _ana2color = '#ffffff' # X11 color: 'white'
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  \
            "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        root.geometry("1366x768+0+0")
        root.config(bg="gold")
        root.state("zoomed")
        root.title("Amrita Vidyalayam")
        root.configure(background="#d9d9d9")
        root.configure(highlightbackground="#d9d9d9")
        root.configure(highlightcolor="black")
        


        self.menubar = Menu(root,font=font9,background='red',fg='green')
        
       

        
       

        self.Frame1 = Frame(root)
        self.Frame1.place(x=0,y=0,width=1366,height=768)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#FF6103")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=925)

        
          
           

        detailframe=Frame(root,bd=4,relief=RIDGE,bg='#191970')
        detailframe.place(x=0,y=0,width=1366,height=150)

        photo = PhotoImage(file = r"H:\School\img\amrits.png")
        photoimage = photo.subsample(3,3)

        photo2 = PhotoImage(file = r"H:\School\img\amma.png")
        photoimage2 = photo2.subsample(5,5)

        title = Label(detailframe, text="Amrita Vidyalayam Senior Secondary CBSE\n Mangalam,Tirupur", font=("Barcade Bold",33, "normal"),bg='#191970', fg="white")
        title.grid(row=0, columnspan=1, padx=200, pady=0, sticky="w")
        title = Label(detailframe,image=photoimage2,compound=RIGHT)
        title.grid(row=0, columnspan=1, padx=1220, pady=10, sticky="w")
        title = Label(detailframe,image=photoimage,compound=LEFT)
        title.grid(row=0, columnspan=1, padx=10, pady=10, sticky="w")

        date=dt.datetime.now()
        format_date=f"{date:%a, %b %d %Y}"
        label=Label(detailframe, text=format_date, font=("Calibri", 20,'bold'),background = '#191970',foreground ='white')
        label.grid(row=0, columnspan=1, padx=150, pady=10,sticky="sw")

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl=Label(detailframe, font = ('calibri', 20, 'bold'),
            background = '#191970',
            foreground = 'white')
        lbl.grid(row=0, columnspan=1, padx=1060, pady=10,sticky="sw")
        time()



        images = ["img\\1.jpg", "img\\2.jpg", "img\\3.jpg",'img\\4.jpg','img\\5.jpg','img\\6.jpg','img\\7.jpg','img\\8.jpg','img\\9.jpg','img\\10.jpg','img\\11.jpg','img\\12.jpg','img\\13.jpg','img\\14.jpg','img\\15.jpg','img\\16.jpg','img\\17.jpg','img\\18.jpg','img\\19.jpg','img\\21.jpg','img\\22.jpg','img\\23.jpg','img\\24.jpg']
        photos = cycle(ImageTk.PhotoImage(PIL.Image.open(image)) for image in images)

        def slideShow():
           img = next(photos)
           displayCanvas.config(image=img,)
           displayCanvas.config(anchor=CENTER)
           root.after(2000, slideShow) # 0.05 seconds


        detailframe1=Frame(root,bd=4,bg='skyblue')
        detailframe1.place(x=420,y=180,width=530,height=400)

        displayCanvas = tk.Label(detailframe1)
        displayCanvas.pack()
        root.after(10, lambda: slideShow())        

      
        detailframe2=Frame(root,bd=4,relief=RIDGE,bg='#191970')
        detailframe2.place(x=0,y=590,width=1366,height=150)

        pygame.mixer.init()

        photo3 = PhotoImage(file = r"H:\School\img\princ.png")
        photoimage3 = photo3.subsample(9,9)

        title = Label(detailframe2, text="Principal\n Shri.Vidhyashankar", font=("Lucida Calligraphy",12, "bold"),bg='#191970', fg="white",image=photoimage3,compound=LEFT)
        title.grid(row=0, columnspan=1, padx=0, pady=0, sticky="w")

        photo4 = PhotoImage(file = r"H:\School\img\kg.png")
        photoimage4 = photo4.subsample(4,4)

        title = Label(detailframe2, text="KG Coordinator\nGayatri", font=("Lucida Calligraphy",12, "bold"),bg='#191970', fg="white",image=photoimage4,compound=LEFT)
        title.grid(row=0, columnspan=1, padx=1050, pady=0, sticky="w")

        photo5 = PhotoImage(file = r"H:\School\img\prim.png")
        photoimage5 = photo5.subsample(9,9)

        title = Label(detailframe2, text="Primary\n Chitramani", font=("Lucida Calligraphy",12, "bold"),bg='#191970', fg="white",image=photoimage5,compound=LEFT)
        title.grid(row=0, columnspan=1, padx=400, pady=0, sticky="w")

        photo6 = PhotoImage(file = r"H:\School\img\sec.png")
        photoimage6 = photo6.subsample(5,5)

        title = Label(detailframe2, text="Secondary\n Dharani", font=("Beyond Wonderland",12, "bold"),bg='#191970', fg="white",image=photoimage6,compound=LEFT)
        title.grid(row=0, columnspan=1, padx=800, pady=0, sticky="w")

       

        

      

       

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0, rely=0.20, height=50, width=400)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="teal")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Student's Registartion''')
        self.Button2.configure(width=400)
        self.Button2.configure(command=click_stureg)
        

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0, rely=0.30, height=50, width=400)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="skyblue")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Teacher's Registeration''')
        self.Button3.configure(width=500)
        self.Button3.configure(command=click_teareg)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0, rely=0.40, height=50, width=400)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="gold")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Worker's Registeration''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_workreg)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0, rely=0.50, height=50, width=400)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="coral")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Student's Attendance''')
        self.Button5.configure(width=500)
        self.Button5.configure(command=click_stuatt)


        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0, rely=0.60, height=50, width=400)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Teacher's Attendance''')
        self.Button3.configure(width=500)
        self.Button3.configure(command=click_teaatt)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.71, rely=0.60, height=50, width=400)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="cyan")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=("Lucida Calligraphy",18, "bold"))
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Classwise Attendance Chart''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_clasatt)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.71, rely=0.20, height=50, width=400)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="khaki")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Mark Entry''')
        self.Button6.configure(width=500)
        self.Button6.configure(command=click_mark)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0.71, rely=0.70, height=50, width=400)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="lawn green")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Class 12th Graph''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_clas12)

        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.71, rely=0.30, height=50, width=400)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="SlateBlue1")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Class 10th Graph''')
        self.Button5.configure(width=500)
        self.Button5.configure(command=click_clas10)


        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.71, rely=0.40, height=50, width=400)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="goldenrod1")
        self.Button3.configure(disabledforeground="#bfbfbf")
        self.Button3.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Classwise Mark Graph''')
        self.Button3.configure(width=500)
        self.Button3.configure(command=click_claswise)

        self.Button4 = Button(self.Frame1)
        self.Button4.place(relx=0, rely=0.70, height=50, width=400)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="turquoise3")
        self.Button4.configure(disabledforeground="#bfbfbf")
        self.Button4.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''FEES''')
        self.Button4.configure(width=500)
        self.Button4.configure(command=click_fee)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.71, rely=0.50, height=50, width=400)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="SeaGreen2")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=("Lucida Calligraphy",20, "bold"))
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Transportation''')
        self.Button6.configure(width=500)
        self.Button6.configure(command=click_trans)

    

        root.mainloop()

        


if __name__ == '__main__':
    GUUEST=Avt()


