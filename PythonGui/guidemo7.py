import tkinter
root=tkinter.Tk()
root.geometry('200x200+100+200')
l1=tkinter.Label(root,text='Name:')
l2=tkinter.Label(root,text='Password:')
e1=tkinter.Entry(root)
e2=tkinter.Entry(root)
b1=tkinter.Button(root,text='login')
b2=tkinter.Button(root,text='exit')
c1=tkinter.Checkbutton(root,text='keep me logged in')
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b1.grid(row=3,column=0)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
b2.grid(row=3,column=1)
c1.grid(row=2,column=0,columnspan=2,sticky=tkinter.W)







root.mainloop()