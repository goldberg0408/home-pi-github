# -*- coding: utf-8 -*
import requests,json

try:
 response = requests.get('https://api.coolsms.co.kr/sms/2/new_group')
 if response.status_code==200:
  data=json.loads(response.text)
  print (data)
 else :
  print ("서버와 연결 되어있지 않습니다")


except:
 print ("서버와 연결 되어있지 않습니다")

#print(data['text'])
#print(data['call'])

