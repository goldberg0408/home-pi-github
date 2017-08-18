# coding:utf-8
import os
import time
import string

os.system("sudo pkill uv4l")

os.system("sudo /etc/init.d/motion restart")
os.system("sudo modprobe bcm2835-v4l2")


question=str(input("폴더내의 이미지파일들을 지우겠습니까? [y/n]"))
print (question)
if question == 'y':
	st= os.walk('/home/pi/motionPicture').next()[2]
	print(st)
	for i in st:
		os.system("sudo rm -f /home/pi/motionPicture/"+i)
		print(i+":clear")

else :
	pre_len = len(os.walk('/home/pi/motionPicture').next()[2])
	print ("first : " + str(pre_len))
	while True:
		crt_len = len(os.walk('/home/pi/motionPicture').next()[2])
		print (pre_len,crt_len)
		if pre_len != crt_len:
			print("motion detectsc")
			pre_len = crt_len
		time.sleep(1)
