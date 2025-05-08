from tkinter import *
import pandas

window = Tk()
window.title("Simple")
window.geometry("600x600")
window.configure(bg="yellow",borderwidth=50)
frame1 = Frame(window, width=200, height=200, cursor="dot")
frame2 = Frame(window, width=200, height=200, cursor="dotbox")
button1 = Button(frame1, text="Click Me", bg = "blue")
button2 = Button(frame2, text="Hit Me", bg = "red")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
# inp = Label(window, text="Hello World")
# inp.pack()
window.mainloop()
'''

import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.geometry("200x100")

label = tk.Label(root, text="Tkinter is working!")
label.pack(pady=20)

root.mainloop()
'''