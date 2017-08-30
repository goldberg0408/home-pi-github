# -*- coding: utf-8 -*
import serial
import time

ser = serial.Serial('/dev/ttyUSB0',9600)
ser.close()


while 1:
	order=raw_input("명령을  입력하세요")

	order =order + '\n'

	try:
		ser.open()
		ser.write(order)
		test=ser.readline()
		print test

		

	except:
		print "fail!"

	ser.close()
