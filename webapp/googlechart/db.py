# -*- coding: utf-8 -*
import MySQLdb
import time
number1 =1
number2 =2
while 1:
	number1 +=1
	number2 +=3
	
	try: 
		db =MySQLdb.connect("localhost","root","1234","atmega128")
                cur= db.cursor()
		cur.execute("insert into ADC(ch_1,ch_2) values('%s','%s')" %(number1,number2))
        	db.commit()
		print "데이터베이스에 값을 넣습니다"
	except:
		print "faill"

	time.sleep(1)
