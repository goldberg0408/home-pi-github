# -*- coding: utf-8 -*
import MySQLdb
import time
import serial
ser = serial.Serial('/dev/ttyUSB0',9600)
ser.close()
def read_range():
	ser.open()
	range = ser.readline()
	ser.close()
	print range
	return range

while 1:
	range = read_range()

	
	try: 
		db =MySQLdb.connect("localhost","root","1234","atmega128")
                cur= db.cursor()
		cur.execute("insert into ADC(ch_1,ch_2) values('%s','%s')" %(range,0))
        	db.commit()
		print "데이터베이스에 값을 넣습니다"
	except:
		print "faill"

	time.sleep(1)
