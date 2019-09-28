from tkinter import *
def changecolor(e):
    root.config(bg="red")
def changecolor1(r):
    root.config(bg="blue")
root=Tk()
root.geometry('200x200')
b1=Button(root,text="Click me")
b1.pack()
b1.bind("<Button-1>",changecolor1)
b1.bind("<Button-3>",changecolor)
root.mainloop()