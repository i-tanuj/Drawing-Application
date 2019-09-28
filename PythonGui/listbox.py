from tkinter import  *
from tkinter import simpledialog,messagebox
root=Tk()
root.geometry("200x200")
lb1=Listbox(root)
sports=["cricket","football","hockey","snooker","rugby"]
for s in sports:
    lb1.insert(END,s)
lb1.grid(row=1,column=0,sticky=W)
messagebox.showinfo("Total items!","No of items in ListBox is: "+str(lb1.size()))
root.mainloop()