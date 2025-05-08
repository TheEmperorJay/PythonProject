from tkinter import *
from tkinter.ttk import *

window = Tk()

window.geometry("500x500")
window.configure(background="white")

var = StringVar()
message = Message(window, textvariable= var, relief= RAISED)
var.set("Hello World")
message.pack()

window.mainloop()