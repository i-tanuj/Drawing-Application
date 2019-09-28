from threading import *
class MyThread(Thread):
	def __init__(self):
		super.__init__()
	def run(self):
		print("Welcome from show !")
		print("this code is executed by:",current_thread().getName())		
print("Welcome to python !")
print("this code is executed by:",current_thread().getName())
my=MyThread()
print("Welcome back !")
print("this code is executed by:",current_thread().getName())