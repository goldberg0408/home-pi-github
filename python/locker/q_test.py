# -*- coding: utf-8 -* 
import queue
import threading

queue =queue.Queue(5)

def thread_1():
   print ("FIFO 방식으로 데이터를 넣음")
   for i in range(5):
     queue.put(i)
     print (i)
   print ("-----------------------")
if __name__ == '__main__':

 t1 =threading.Thread(target=thread_1)
 t1.start()
 t1.join()
 while queue.qsize():
  print (queue.get())
