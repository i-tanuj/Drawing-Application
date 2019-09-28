import datetime
import tkinter
root=tkinter.Tk()
def greet():
    current=datetime.datetime.now()
    x=current.strftime("%d-%b-%Y")
    l1.config(text=x)
root.geometry('200x200')
b1=tkinter.Button(root,text='click me',command=greet)
b1.pack()
l1=tkinter.Label(root,text='click button to show date and time')
l1.pack()
root.mainloop()