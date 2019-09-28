from tkinter import *
oldcolor=""

def changecolor(e):
    if e.char=="r":
        root["bg"]="red"
    elif e.char=="g":
        root["bg"]="green"
    elif e.char=="b":
        root["bg"]="blue"
root = Tk()
root.geometry('200x200')
root.bind("<Key>",changecolor)
root.mainloop()
