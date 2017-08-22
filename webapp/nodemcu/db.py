# -*- coding: utf-8 -* 
import json
import time
import MySQLdb
import serial

try:
        from urllib.request import urlopen
except ImportError:
        from urllib2 import urlopen

base_url ="http://192.168.1.141:8888"
events_url = base_url + "/events"
ser =serial.Serial('/dev/ttyUSB0',9600)
ser.close()
def read_range():
	ser.open()
	range = ser.readline()
	ser.close()
	print range
	return range


while 1:
	db = MySQLdb.connect("localhost","root","1234","DHT11")
	cur = db.cursor()
	u =urlopen(events_url)
        data = ""
        try:
                data=u.read()
                t =data.decode('utf8')
                go = json.loads(t)
                print (go["temp"])
		print (go["humi"])
		print ("온도 습도 값을 데이터 베이스에 넣습니다")
        except:
                print ("fail !")

	cur.execute("insert into DHT_11(temp,humi) values('%s','%s')" %(go["temp"],go["humi"]))
	db.commit()

	cur.close()
	db.close()

	try:
		range =read_range()

		db1=MySQLdb.connect("localhost","root","1234","atmega128")
		cur1=db1.cursor()

		cur1.execute("insert into ADC(ch_1,ch_2) values('%s','%s')" %(range,0))
		db1.commit()
		print ("거리값을 데이터베이스에 넣습니다")
	except:
		print ("fail !!")

	
	cur1.close()
	db1.close()


	time.sleep(1)

