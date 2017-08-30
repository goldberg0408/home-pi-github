# -*- coding: utf-8 -*
import serial
import time
import os

try:
	os.system('sudo rfcomm bind rfcomm0 20:15:12:15:02:64')
	ser = serial.Serial('/dev/rfcomm0',115200)
except:
	print "연결 실패 하였습니다"
	print "기기 페어링이 완료 되었는지 확인 해보세요"

while 1:
	order =raw_input("명령을 입력하세요")

	order =order + '\n'

	try:
		ser.write(order)
		print ser.readline()

	except:
		print "fail!"


