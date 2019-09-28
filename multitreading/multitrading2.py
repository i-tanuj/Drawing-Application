from threading import *
def show():
	for i in range(10):
		print(current_thread().getName()+" : ping")
th=Thread(target=show,name="Tanuj Thread")
th.start()
for i in range(10):
		print(current_thread().getName()+" : ping")
