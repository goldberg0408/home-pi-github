import time
from multiprocessing import Process,pool

def test():
 start_time=time.time()

 for i in range(10000000):
  pase=1

 print ("%s" %(time.time()-start_time))

if __name__=='__main__':

 p = Process(target=test)
 p.start()
 p.join()
