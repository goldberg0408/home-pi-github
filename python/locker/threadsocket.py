import threading
import serial
from socket import *
import time

def socket_th():
 HOST='192.168.1.169' #플라스크서버의 ip 주소
 while 1:
  ser = serial.Serial('/dev/ttyUSB0',9600) # 시리얼 통신 포트
  ser.close()

  c = socket(AF_INET, SOCK_STREAM) # 소켓 객체 생성
  try:
   c.connect((HOST,5002)) #소켓 서버 해당 호스트,포트번호로 연결
   data=c.recv(10) #서버로부터 데이터를 받음
   print (data) #받은 데이터 출력
   ser.open() #시리얼 통신 객체 포트 open
   enco = "\r"
   data = data+enco.encode()
   ser.write(data) # mcu측으로 데이터 보냄
   atmega=ser.readline() #mcu측으로부터 데이터를 받음
   print(atmega)
   ser.close() #시리얼 통신 포트 객체 소멸

  except:
   pass
  c.close() #소켓 서버 객체 소멸
  del c

t1 = threading.Thread(target=socket_th)
#t1.daemon=True
t1.start()


