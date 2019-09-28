import tkinter
root = tkinter.Tk()
msg=tkinter.StringVar()
lbl=tkinter.Label(root,borderwidth=2,relief="solid",textvariable=msg)
lbl.pack()
msg.set("Welcome")
root.mainloop()