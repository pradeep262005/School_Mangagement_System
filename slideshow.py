import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image

images = ["1.jpeg", "2.jpeg", "3.jpeg"]
photos = cycle(ImageTk.PhotoImage(Image.open(image)) for image in images)

def slideShow():
  img = next(photos)
  displayCanvas.config(image=img)
  root.after(1000, slideShow) # 0.05 seconds

root = tk.Tk()
root.geometry('1366x768')
displayCanvas = tk.Label(root)
displayCanvas.pack()
root.after(10, lambda: slideShow())
root.mainloop()
