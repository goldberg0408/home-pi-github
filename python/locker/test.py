# -*- coding: utf-8 -*
import serial


ser = serial.Serial('/dev/ttyUSB0',9600)
ser.close()
while 1:
 ser.open()
 response = ser.read(10)
 #data=response.decode('utf-8')
 ser.close()
 print (str(response))
