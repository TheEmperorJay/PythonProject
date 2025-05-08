from tkinter import *
window = Tk()
window.title("Calculator")

window.geometry("500x500")
window.configure(background="white")

#ENTRYBOX
eb = Entry(window, width=56, borderwidth=5)
eb.place(x=0, y=0)

def click(num):
    result = eb.get()
    eb.delete(0, END)
    eb.insert(0, str(result) + str(num))



#Buttons
b = Button(window, width=13, text=1, relief=RAISED, command= lambda :click(1))
b.place(x=10, y=60)
b = Button(window, width=13, text=2, relief=RAISED, command= lambda :click(2))
b.place(x=160, y=60)
b = Button(window, width=13, text=3, relief=RAISED, command= lambda :click(3))
b.place(x=310, y=60)
b = Button(window, width=13, text=4, relief=RAISED, command= lambda :click(4))
b.place(x=10, y=120)
b = Button(window, width=13, text=5, relief=RAISED, command= lambda :click(5))
b.place(x=160, y=120)
b = Button(window, width=13, text=6, relief=RAISED, command= lambda :click(6))
b.place(x=310, y=120)
b = Button(window, width=13, text=7, relief=RAISED, command= lambda :click(7))
b.place(x=10, y=180)
b = Button(window, width=13, text=8, relief=RAISED, command= lambda :click(8))
b.place(x=160, y=180)
b = Button(window, width=13, text=9, relief=RAISED, command= lambda :click(9))
b.place(x=310, y=180)
b = Button(window, width=13, text=0, relief=RAISED, command= lambda :click(0))
b.place(x=160, y=240)
b = Button(window, width=13, text=".", relief=RAISED)
b.place(x=310, y=240)

def mul():
    n1 = eb.get()
    global math
    math = "Multiplication"
    global i
    i = int(n1)
    eb.delete(0, END)

b = Button(window, width=13, text="*", relief=RAISED, command= mul)
b.place(x=10, y=240)

def add():
    n1 = eb.get()
    global math
    math = "Addition"
    global i
    i = int(n1)
    eb.delete(0, END)

b = Button(window, width=13, text="+", relief=RAISED, command=add)
b.place(x=10, y=300)

def sub():
    n1 = eb.get()
    global math
    math = "Subtraction"
    global i
    i = int(n1)
    eb.delete(0, END)

b = Button(window, width=13, text="-", relief=RAISED, command=sub)
b.place(x=160, y=300)

def div():
    n1 = eb.get()
    global math
    math = "Division"
    global i
    i = int(n1)
    eb.delete(0, END)

b = Button(window, width=13, text="/", relief=RAISED, command=div)
b.place(x=310, y=300)

def eq():
    n2 = eb.get()
    eb.delete(0, END)
    if math == "Multiplication":
        eb.insert(0,i * int(n2))
    elif math == "Subtraction":
        eb.insert(0,i - int(n2))
    elif math == "Division":
        eb.insert(0,i / int(n2))
    elif math == "Addition":
        eb.insert(0,i + int(n2))

b = Button(window, width=21, text="=", relief=RAISED, command=eq)
b.place(x= 10, y=360)

def clear():
    eb.delete(0, END)

b = Button(window, width=21, text="clear", relief=RAISED, command=clear)
b.place(x= 237, y=360)
mainloop()