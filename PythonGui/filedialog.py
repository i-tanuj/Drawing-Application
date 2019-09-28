import os
from tkinter import *
from tkinter import filedialog, messagebox

def showopen():
    fname=filedialog.askopenfilenames(title="Select your fav song",filetypes=[("mp3 files","*.mp3")])
    if len(fname)==0:
        messagebox.showinfo("No selection","you did not select any song")
    else:
        str=""
        for file in fname:
           str=str+file+"\n"
        lbl.configure(text=str)
        return str
root = Tk()
root.geometry("200x200")
btn=Button(root,text="Open File",command=showopen)
lbl=Label(root,text="you select song to display this window")
lbl.pack()
btn.pack()
root.mainloop()
