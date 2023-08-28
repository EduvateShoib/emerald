from tkinter import *
from tkinter.ttk import *

def show():
    print("Button Clicked")


win1 = Tk()
win1.geometry("400x400")

l1 = Label(win1, text="Python is Awesome", font=("arial",20,"bold"))
l1.pack()

b1 = Button(win1, text="Submit", command=show)
b1.pack()

menubar = Menu(win1)

file = Menu(menubar, tearoff = 0)
file.add_command(label="New File")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Open")
file.add_command(label="Exit", command=win1.destroy)

menubar.add_cascade(label = "File", menu = file)



edit = Menu(menubar, tearoff = 0)
edit.add_command(label="New File")
edit.add_command(label="Save")
edit.add_command(label="Save As")
edit.add_command(label="Open")
edit.add_command(label="Exit", command=win1.destroy)

menubar.add_cascade(label = "Edit", menu = edit)



win1.config(menu = menubar)
win1.mainloop()
