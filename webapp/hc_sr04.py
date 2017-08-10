# coding :utf-8
import serial
import time
import httplib,urllib

headers = {"Content-type":"application/x-www-form-urlencoded","Accept":"text/plain"}
KEY = 'I97Q0C9RMV3GAJX4'
DEBUG=True
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.close()

def read_range():
	ser.open()
	range = ser.readline()
	ser.close()
	print range
	return range
while True:
	range=read_range()
	params =urllib.urlencode({'field1':range, 'key':KEY})
	conn =httplib.HTTPConnection("api.thingspeak.com:80")
	
	try:
		conn.request("POST","/update",params,headers)
		response = conn.getresponse()
		if DEBUG:
			print response.status, response.reason
		data = response.read()
		conn.close()
	except:
		print "connection fail!!!"

	time.sleep(1)

