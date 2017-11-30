import threading
import os

def thread_1():
   os.system("omxplayer -o local dust_bad.mp3")

#def thread_2():
  # os.system("omxplayer -o local led2.wav")


t1 = threading.Thread(target=thread_1)
#t2 = threading.Thread(target=thread_2)

t1.start()
print (t1.isAlive())
t1.join()
print (t1.getName())
print (t1.isAlive())
#t2.start()
