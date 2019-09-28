import tkinter
tw=tkinter.Tk()
lbl=tkinter.Label(tw,text="Hello\nIndia",borderwidth=2,relief="solid",width=20,height=4,anchor="w")
lbl.pack()
lbl["bg"]="yellow"
tw.mainloop()