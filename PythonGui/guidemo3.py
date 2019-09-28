import tkinter
tw = tkinter.Tk()
tw.title("My Gui App")
img=tkinter.PhotoImage(file="F:\Study Materials\SCA\PYTHON\Project\icons\Vinylrecord.png")
tw.iconphoto(tw,img)
screenwidth=tw.winfo_screenwidth()
screenheight=tw.winfo_screenheight()
width=screenwidth//2
height=screenheight//2
xco=screenwidth//4
yco=screenheight//4
tw.geometry(f"{width}x{height}+{xco}+{yco}")
tw.resizable(False,False)
tw.mainloop()