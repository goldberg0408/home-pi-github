# -*- coding: utf-8 -*
import requests,json
import serial
try:
 ser = serial.Serial('/dev/ttyUSB0',9600)
 ser.close()
except:
 print ("제어기기와 연결 되어있지 않습니다")

try:
 response = requests.post('http://192.168.1.169:5001/post')
 if response.status_code==200:
  data=json.loads(response.text)
  ser.open()
  ser.write(data['text'].encode()) #byte형으로 바꿔줌
  atmega=ser.readline()
  data_atmega = atmega.decode('utf-8') #string형으로 바꿔줌
  print (data_atmega)
  ser.close()
 else :
  print ("서버와 연결 되어있지 않습니다")


except:
 print ("서버와 연결 되어있지 않습니다")

#print(data['text'])
#print(data['call'])

