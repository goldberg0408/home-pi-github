#-*- coding:utf-8 -*-
#파이썬3으로 동작 시킬것

import json
import requests

params = {"version": "1", "city":"부산", "county":"수영구","village":"광안동"} #딕셔너리 형식 - 사용하기 편리하다.
headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}
r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)


#json 라이브러리 사용 파싱
#json -> python 객체로 변환
data = json.loads(r.text)
weather = data["weather"]["hourly"]
cTime = weather[0]["timeRelease"]
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]

#print (r.json()) #json형태로 출력
#print(data)
#종합하면 
cWeather = "오늘의 날씨 "+cTime+" 기준 하늘은 '" +cSky+ "'상태이고 풍속은" + cWind + "이고 기온은 " + cTemp + "입니다."
print(cWeather)
