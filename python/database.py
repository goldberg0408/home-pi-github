# -*- coding: utf-8 -* 
import MySQLdb

def db_excute(a):
        execute_a = "select * from sttall where text1='"+a
        execute_a = execute_a + "'"
#        print execute_a
        return execute_a


while (1):
	  try :
       		 print ("데이터베이스 접속 시도중...")
        	 db=MySQLdb.connect(host="localhost",user="root",passwd="1234",db="stt")
        	 print "데이터 베이스 접속 성공"
		 print "----------------------"
	  except :
        	 print "데이터 베이스 접속 실패"


	  test=raw_input("짭비스:나를 불러 보세요->") # stt로 문자열 받는것
	  print "-------------------"


	  try:
		cur = db.cursor()
	 	cur.execute(db_excute(test))
		rs =cur.fetchone()
		repr(rs[1]).decode('string-escape')
		print rs[1]
		if rs[1] == 'call':
		 comm = raw_input("짭비스: 하실 말씀이 있으신가요->") # stt로 문자열 받는 것 
		 print "---------------------"
		 cur=db.cursor()
		 cur.execute(db_excute(comm))
		 rs =cur.fetchone()
		 if rs[1] =='turnon': #실질적인 mcu로 통신 제어 문 보내면 되겠다.
			print "짭비스:불을 키겠습니다"
			print "---------------------"
		 elif rs[1]=='led:1':
			print "led 1번을 키겠습니다"
			print "-------------------"
		 elif rs[2]=='led:2':
			print "led 2번을 키겠습니다"
			print "--------------------"


	  except:
		print "짭비스:무슨말인지 모르겠네요"
		print "-----------------------------"


	  cur.close()
	  db.close()


