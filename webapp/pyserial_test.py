# coding :utf-8
import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.close()

while 1:
	ser.open()
	response = ser.readline()
	ser.close()
	print response

	split_data=response.split(',')
	print(split_data[0])
	print(split_data[1])
