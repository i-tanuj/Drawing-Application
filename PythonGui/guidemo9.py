from tkinter import *
def greet():
    l1.config(text='welcome to python')
root=Tk()
root.geometry('200x200')
b1=Button(root,text='click me',command=greet)
l1=Label(root)
l1.pack()
b1.pack()


root.mainloop()