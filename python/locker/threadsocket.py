import threading
import serial
from socket import *
import time
import pymysql
import requests,json
lock = threading.Lock()
def socket_th():
 HOST='192.168.1.163' #플라스크서버의 ip 주소
 while 1: 
  c = socket(AF_INET, SOCK_STREAM) # 소켓 객체 생성
  try:
   c.connect((HOST,5002)) #소켓 서버 해당 호스트,포트번호로 연결
   ser = serial.Serial('/dev/ttyUSB0',9600,timeout=10) # 시리얼 통신 포트
   ser.close()

   data=c.recv(10) #서버로부터 데이터를 받음
   print (data) #받은 데이터 출력
   ser.open() #시리얼 통신 객체 포트 open
   enco = "\r"
   data = data+enco.encode()

   lock.acquire() #lock을 획득
   ser.write(data) # mcu측으로 데이터 보냄
   atmega=ser.readline() #mcu측으로부터 데이터를 받음
   lock.release() #lock을 풀어줌


   print ("쓰레드로 받은 데이터")
   if atmega == b'':
     print ("db삭제안함")
   else :
     print(atmega)
   ser.close() #포트 닫음

  except:
   pass
  finally:
   c.close() #소켓 서버 객체 소멸
   del c

def thread_2():
   db = pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem",charset="utf8")
   cur  =db.cursor()
   cur.execute("select * from m_info where sec_key='qeqe'")
   rs = cur.fetchone()
   print (rs)

   data = {"location":rs[2],
           "name":rs[3],
           "phone":rs[4],
           "sec_key":rs[5],
           "box_num":rs[6]} 
   try:
     response = requests.post('http://192.168.1.163:5000/find',data=data) #db로 받은 데이터 메인으로 요청 ,데이터 보냄
     print (response.status_code)
     data=json.loads(response.text)


     if data['verify']=='OK':
       print ("문자 전송 완료")

     else : #문자 전송 실패 
       print (data['verify'])

   except:
     print ("서버 접속 실패")


if __name__ =='__main__':

 t1 = threading.Thread(target=socket_th)
 t2 = threading.Thread(target=thread_2)
 t1.start()
 #t2 = threading.Thread(target=thread_2)
 t2.start()
 #time.sleep(1)
 #lock = threading.Lock()
