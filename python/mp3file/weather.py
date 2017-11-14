# -*- coding: utf-8 -* 

import json
import requests
import os
params = {"version": "1", "city":"부산", "county":"수영구","village":"광안동"} #딕셔너리 형식 - 사용하기 편리하다.
headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}
r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)

#json 라이브러리 사용 파싱
#json -> python 객체로 변환
data = json.loads(r.text)
weather = data["weather"]["hourly"] #hourly 하위 내용들을 weather 에 모두 저장 
cTime = weather[0]["timeRelease"]
cSky = weather[0]["sky"]["name"]
cWind = weather[0]["wind"]["wspd"]
cTemp = weather[0]["temperature"]["tc"]
precipitation =weather[0]["precipitation"]["sinceOntime"]#강수량
Tmax = weather[0]["temperature"]["tmax"]
hump = weather[0]["humidity"]

#cSky=unicode_string.encode("utf-8")
print cTemp
print cSky

if cSky.encode("utf-8")=='구름많음':
	os.system("omxplayer cloudy2.wav")
