import threading
import serial
from socket import *
import time

import requests,json
lock = threading.Lock()
def socket_th():
 HOST='192.168.1.163' #플라스크서버의 ip 주소
 while 1: 
  c = socket(AF_INET, SOCK_STREAM) # 소켓 객체 생성
  try:
   c.connect((HOST,5002)) #소켓 서버 해당 호스트,포트번호로 연결
   ser = serial.Serial('/dev/ttyUSB0',9600) # 시리얼 통신 포트
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
   print(atmega)
   ser.close() #포트 닫음

  except:
   pass
  c.close() #소켓 서버 객체 소멸
  del c


if __name__ =='__main__':

 t1 = threading.Thread(target=socket_th)
 t1.start()
 #lock = threading.Lock()
 while 1:
   data = {"key_value":"abcd"} #메인서버로 db에 데이터가 있는지 확인차 보내는 것
   response = requests.post('http://192.168.1.163:5000/find',data=data)


   print (response.status_code)
   data=json.loads(response.text)


   if data['verify']=='OK':
      print (data['comm'])
      
      lock.acquire() #락을 얻음
      ser = serial.Serial('/dev/ttyUSB0',9600)
       #ser.close()
       #ser.open()
      enco = "\r"
      com = data['comm'].encode()+enco.encode()
      ser.write(com)
      #lock.acquire()
      atmega =ser.readline()
      lock.release()
      print ("일반데이터")
      print(atmega)
      ser.close()
      del ser
      
       
   else : #데이터베이스에 없으면 FAIL이라는 문자열 반환
      print (data['verify'])

   time.sleep(1)

