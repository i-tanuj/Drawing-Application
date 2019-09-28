from tkinter import *
import time
from threading import *
class MyFirstGUI:
      def __init__(self):
          self.root= root
          self.root.title("An OOP GUI")
          self.root.geometry('300x200')
          self.click_Button(self.root,text="Click Me",command=self.setup_thread)
          self.click_Button.pack()
          self.stop_Button.pack()
          self.shouldstop=FALSE
      def setup_thread(self):
            th.Thread(target=self.counter)
            th.start()
      def counter(self):

root.mainloop()
