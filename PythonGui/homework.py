from tkinter import *
from tkinter import simpledialog,messagebox
def divide():
    try:
        e3.delete(0, END)
        e3.config(fg="red")
        a=int(e1.get())
        b=int(e2.get())
        c=a/b
        e3.config(fg="green")
        e3.insert(0,str(c))
    except ZeroDivisionError:
        messagebox.showerror("Arthimetic error!","Denominator should be positive")
    except ValueError:
        messagebox.showerror("Wrong input!","only digits are allow")

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.focus()

def finish():
    name=simpledialog.askstring("Enter name","what is your name")
    if name is not None:
        messagebox.showinfo("Welcome","Thankyou For Using This App "+name)
    root.destroy()
root = Tk()
root.geometry('400x200+100+200')
l1=Label(root, text="Number Division Program",font="Arial 18 bold")
l2=Label(root, text="First No:")
l3=Label(root, text="Second No:")
l4=Label(root,text="Result:")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="Divide",command=divide)
b2=Button(root,text="Clear",command=clear)
b3=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
l4.grid(row=3,column=0,sticky=E)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
root.mainloop()
