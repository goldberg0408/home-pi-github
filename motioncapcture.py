import os
import time

pre_len = len(os.walk('/home/pi/motionPicture').next()[2])
print ("first : " + str(pre_len))
while True:
    crt_len = len(os.walk('/home/pi/motionPicture').next()[2])
    print (pre_len, crt_len)
    if pre_len != crt_len:
        print("motion detectsc")
        pre_len = crt_len
    time.sleep(1)
