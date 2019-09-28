import threading
def show():
	print("Welcome to python !")
	print("This code execute by ",threading.current_thread().getName())

print("Welcome to python !")
print("This code execute by ",threading.current_thread().getName())
th=threading.Thread(target=show)
th.start()
print("Welcome back")
print("This code execute by ",threading.current_thread().getName())