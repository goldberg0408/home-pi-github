import json
import requests
import time

params = {"version": "1", "lon":"128.58498400000","lat":"35.124540000000"} #딕셔너리 형식 - 사용하기 편리하다.

headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}

while True:

  r = requests.get("http://apis.skplanetx.com/weather/dust", params=params, headers=headers)

  #json 라이브러리 사용 파싱
  #json -> python 객체로 변환
  data = json.loads(r.text)
  weather = data["weather"]["dust"]
  station = weather[0]["station"]["name"]#측정소 정보와 측정소 명이다
  dtime =weather[0]["timeObservation"] #관측시간을 나타냄
  value = weather[0]["pm10"]["value"] #미세먼지의 농도를 나타낸다
  grade = weather[0]["pm10"]["grade"] #미세먼지의 등급을 나타냄
  print (station)
  print (dtime)
  print (value)
  print (grade)

  time.sleep(5)
