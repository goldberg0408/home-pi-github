from multiprocessing import Process,Pool
import threading
import time

def thread_1():
 print ("thread 1 start")
 start_time =time.time()
 for i in range(10000000):
  pase=1;
 print ("thread 1 time :%s" %(time.time()-start_time))

def thread_2():

 start_time = time.time()
 for i in range(10000000):
  pase =1;
 print ("thread 2 time : %s" %(time.time()-start_time))


def process_1():
 t1 = threading.Thread(target=thread_1)
 t1.start()
 t1.join()

def process_2():

 t1 = threading.Thread(target=thread_1)
 t2 = threading.Thread(target=thread_2)
 t1.start()
 t2.start()
 t1.join()
 t2.join()

if __name__ =='__main__':

 p1 = Process(target=process_1)
 p2 = Process(target=process_2)
 p1.start()
 p2.start()

 p1.join()
 p2.join()
