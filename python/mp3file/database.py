# -*- coding: utf-8 -*
#파이썬 3에서 동작 
import pymysql
import os
import time
import json
import requests

import sys
import urllib.request
#import urllib
from socket import *


def weather():
 print ("날씨 데이터를 읽어오는 중입니다 ..잠시만 기다려주세요")
 params = {"version": "1", "city":"부산", "county":"수영구","village":"광안동"} #딕셔너리 형식 - 사용하기 편리하다.
 headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}
 r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)
 #json 라이브러리 사용 파싱
 #json -> python 객체로 변환
 data = json.loads(r.text)
 weather = data["weather"]["hourly"] #hourly 하위 내용들을 weather 에 모두 저장
 cTime = weather[0]["timeRelease"]
 sky = weather[0]["sky"]["name"]
 temp = weather[0]["temperature"]["tc"]
 precipitation =weather[0]["precipitation"]["sinceOntime"]
 tmax = weather[0]["temperature"]["tmax"]
 hump = weather[0]["humidity"]

 #print ("날씨 데이터를 받는 중입니다 잠시만 기다려주세요...")
 text ="오늘 날씨는"+sky+"이고\r\n"+"현재온도는"+temp+"도 입니다.\r\n"+"그리고 최고온도는"+tmax+"도 입니다.\r\n"
 client_id = "h1pO8IUrZsmwiGRqY_dQ"
 client_secret = "fDoPMVSaCA"
 encText = urllib.parse.quote(text)
 data = "speaker=jinho&speed=1&text=" + encText;
 url = "https://openapi.naver.com/v1/voice/tts.bin"
 request = urllib.request.Request(url)
 request.add_header("X-Naver-Client-Id",client_id)
 request.add_header("X-Naver-Client-Secret",client_secret)
 response = urllib.request.urlopen(request, data=data.encode('utf-8'))
 rescode = response.getcode()
 if(rescode==200):
  print("음성합성완료")
  response_body = response.read()

  with open('wether.mp3', 'wb') as f:
   f.write(response_body)
   os.system("omxplayer wether.mp3")
 else:
  print("Error Code:" + rescode)



 if sky=='맑음':
   os.system("omxplayer sunny.mp3")
 elif sky=='구름조금':
   os.system("omxplayer sky_002.mp3")
 elif sky=='구름많음':
   os.system("omxplayer sky_003.mp3")
 elif sky=='구름많고 비' or sky=='구름많고 눈' or sky=='구름많고 비 또는 눈':
   os.system("omxplayer sky_005.mp3")
 elif sky=='흐림' or sky=='흐리고 비' or sky=='흐리고 눈':
   os.system("omxplayer sky_006.mp3")
 else :
   os.system("omxpayer sky_004.mp3")


def dust():

  params = {"version": "1", "lon":"128.58498400000","lat":"35.124540000000"} #딕셔너리 형식 - 사용하기 편리하다.
def dust():

  params = {"version": "1", "lon":"128.58498400000","lat":"35.124540000000"} #딕셔너리 형식 - 사용하기 편리하다.

  headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}


  r = requests.get("http://apis.skplanetx.com/weather/dust", params=params, headers=headers)

  #json 라이브러리 사용 파싱
  #json -> python 객체로 변환
  data = json.loads(r.text)
  weather = data["weather"]["dust"]
  station = weather[0]["station"]["name"]#측정소 정보와 측정소 명이다
  dtime =weather[0]["timeObservation"] #관측시간을 나타냄
  value = weather[0]["pm10"]["value"] #미세먼지의 농도를 나타낸다
  grade = weather[0]["pm10"]["grade"] #미세먼지의 등급을 나타냄

  text ="오늘 미세먼지 수치는 "+value+"이고, 등급은"+grade+"입니다."

  headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}


  r = requests.get("http://apis.skplanetx.com/weather/dust", params=params, headers=headers)

  #json 라이브러리 사용 파싱
  #json -> python 객체로 변환
  data = json.loads(r.text)
  weather = data["weather"]["dust"]
  station = weather[0]["station"]["name"]#측정소 정보와 측정소 명이다
  dtime =weather[0]["timeObservation"] #관측시간을 나타냄
  value = weather[0]["pm10"]["value"] #미세먼지의 농도를 나타낸다
  grade = weather[0]["pm10"]["grade"] #미세먼지의 등급을 나타냄

  text ="오늘 미세먼지 수치는 "+value+"이고, 등급은"+grade+"입니다."

  client_id = "h1pO8IUrZsmwiGRqY_dQ"
  client_secret = "fDoPMVSaCA"
  encText = urllib.parse.quote(text)
  data = "speaker=jinho&speed=2&text=" + encText;
  url = "https://openapi.naver.com/v1/voice/tts.bin"
  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request, data=data.encode('utf-8'))
  rescode = response.getcode()
  if(rescode==200):
   print("음성합성완료")
   response_body = response.read()

   with open('dust.mp3', 'wb') as f:
    f.write(response_body)
    os.system("omxplayer dust.mp3")
  else:
   print("Error Code:" + rescode)

  print (station)
  print (dtime)
  print (value)
  print (grade)
  grade ='나쁨' 
  if grade =='좋음':
   os.system("omxplayer dust_good.mp3")
  elif grade =='보통':
   os.system("omxplayer dust_mid.mp3")
  elif grade == '약간나쁨':
   os.system("omxplayer dust_bad.mp3")
  elif grade == '나쁨' or grade =='매우나쁨':
   os.system("omxplayer dust_bad1.mp3")


def server(host,port,data):
 c = socket(AF_INET,SOCK_STREAM)
 print ('connect to server')
 #os.system("omxplayer serveron.wav")
 try :
  #os.system("omxplayer servercomplete.wav")
  print ('success connect')
  c.connect((host,port))
  c.send(data)
 except:
  print ("fail to connect server")
  #os.system("omxplayer serverfail.wav")
 d=c.recv(1024)
 print(d)
 c.close()





while (1):
 try:
  print ("데이터베이스 접속 시도중 ...")
  db=pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')
  cur = db.cursor()
  test =input("짭비스 : 저를 불러주세요 ->")
  print(test)
  query = "select * from sttall where text1='"+test+"'"
  #repr(test).decode('string-escpae')
  #cur=db.cursor()
  cur.execute(query)
  rs =cur.fetchone()
  #repr(rs[1]).decode('string-escape')
  if rs[1] == 'call':
   os.system("omxplayer call.wav")
   comm = input("짭비스: 하실 말씀이 있으신가요->") # stt로 문자열 받는 것 
   print ("---------------------")
   cur=db.cursor()
   query = "select * from sttall where text1='"+comm+"'"

   cur.execute(query)
   rs =cur.fetchone()
  if rs[1] =='turnon': #실질적인 mcu로 통신 제어 문 보내면 되겠다.
   print ("짭비스:불을 키겠습니다")
   print ("---------------------")
   server('192.168.1.179',8000,rs[1])
   os.system("omxplayer turnon.wav")
  elif rs[1]=='led:1':
   print ("led 1번을 키겠습니다")
   os.system("omxplayer led1.wav")
   print ("-------------------")
  elif rs[1]=='led:2':
   print ("led 2번을 키겠습니다")
   print ("--------------------")
   os.system("omxplayer led2.wav")
  elif rs[1]=='turnoff':
   print ("불을 끄겠습니다")
   server('192.168.1.179',8000,rs[1])
   os.system("omxplayer turnoff.wav")
  elif rs[1]=='led:r':
   print ("빨간색led만 키겠습니다.")
   server('192.168.1.179',8000,rs[1])
  elif rs[1]=='led:g':
   print ("초록색 led만 키겠습니다.")
   server('192.168.1.179',8000,rs[1])
  elif rs[1]=='led:b':
   print ("파란색 led만 키겠습니다.")
   server('192.168.1.179',8000,rs[1])
  elif rs[1]=='weather':
   print ("오늘 날씨입니다")
   weather()
  elif rs[1]=='dust':
   print ("오늘 미세 먼지 ")
   dust()

 except:
  print ("짭비스:무슨말인지 모르겠네요")
  os.system("omxplayer fail.wav")
  print ("-----------------------------")

  #os.system("omxplayer -o local led2.wav")
 cur.close()
 db.close()


