import time
from threading import *
def printsquare(l1):
	for i in l1:
		print("square of ",i,"is",i*i)
		time.sleep(1)
def printcube(l2):
	for i in l2:
		print("cube of ",i,"is",i*i*i)
		time.sleep(1)
being=time.time()
l3=[n for n in range(1,11)]
t1=Thread(target=printsquare,args=(l3,))
t2=Thread(target=printcube,args=(l3,))
t1.start()
t2.start()
t1.join()
t2.join()
end=time.time()
print("Total time taken",end-being,"second")