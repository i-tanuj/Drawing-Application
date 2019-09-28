import tkinter
root = tkinter.Tk()
logo=tkinter.PhotoImage(file="F:/Study Materials/SCA/PYTHON/Project/icons/vinylrecord.png")
lbl=tkinter.Label(root,image=logo,text="CORRECT",compound=tkinter.CENTER)

lbl.pack()
root.mainloop()