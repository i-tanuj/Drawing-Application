import tkinter
tw=tkinter.Tk()
tw.title("My Gui App")
img=tkinter.PhotoImage(file="F:\Study Materials\SCA\PYTHON\Project\icons\Vinylrecord.png")
tw.iconphoto(tw,img)
#tw.geometry("600x400+200+100")
sw=tw.winfo_screenmmwidth()
sh=tw.winfo_screenheight()
ww=sw//2
wh=sh//2
x=sw//4
y=sh//4
tw.geometry(f"{ww}x{wh}+{x}+{y}")
tw.resizable(False,False)
#print(sw,sh)
tw.mainloop()