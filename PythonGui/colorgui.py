from tkinter import *
from tkinter import colorchooser,messagebox
def showopen():
    fcolor=colorchooser.askcolor()
    if fcolor[0] is None:
        messagebox.showinfo("No Color","you did not chose color")
    else:
        root.config(bg=fcolor[1])
root=Tk()
root.geometry("200x200")
btn=Button(root,text="change color",command=showopen)
btn.pack()
root.mainloop()