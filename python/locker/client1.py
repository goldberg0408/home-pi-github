import requests,json
import serial

data = {"key_value":"ddef"} #메인서버로 db에 데이터가 있는지 확인차 보내는 것
response = requests.post('http://192.168.1.163:5000/find',data=data)


print (response.status_code)
data=json.loads(response.text)


if data['verify']=='OK':
      print (data['comm'])
      try:
       ser = serial.Serial('/dev/ttyUSB0',9600)
       #ser.close()
       #ser.open()
       enco = "\r"
       com = data['comm'].encode()+enco.encode()
       ser.write(com)
       atmega =ser.readline()
       print(atmega)
       ser.close()
       del ser
      except:
       pass
else : #데이터베이스에 없으면 FAIL이라는 문자열 반환
      print (data['verify'])
