# -*- coding: utf-8 -*-
#파이썬3에서 동작합니다.
import os
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import abort,redirect,url_for

import pymysql
import json
import requests
import sys
import urllib.request

import re

area_1=" "


def weather(area):
 #print ("날씨 데이터를 읽어오는 중입니다 ..잠시만 기다려주세요")
 db1 = pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')
 cur1 = db1.cursor()
 query = "select * from weather where area='"+area+"'"

 cur1.execute(query)


 rs = cur1.fetchone()
 cur1.close()
 db1.close()
 #params = {"version": "1", "city":"경상남도", "county":"창원시","village":"성주동"} #딕셔너리 형식 - 사용하기 편리하다.
 params = {"version": "1", "lat":rs[1] ,"lon":rs[2]}
 params1 = {"version": "1", "lon":rs[2],"lat":rs[1]}
 headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}
 r = requests.get("http://apis.skplanetx.com/weather/current/hourly", params=params, headers=headers)
 d = requests.get("http://apis.skplanetx.com/weather/dust", params=params1, headers=headers)
 #json 라이브러리 사용 파싱
 #json -> python 객체로 변환
 data = json.loads(r.text)
 dust_data =json.loads(d.text)
 
 #날씨데이터
 weather = data["weather"]["hourly"] #hourly 하위 내용들을 weather 에 모두 저장
 cTime = weather[0]["timeRelease"]
 sky = weather[0]["sky"]["name"]
 temp = weather[0]["temperature"]["tc"]
 precipitation =weather[0]["precipitation"]["sinceOntime"]
 tmax = weather[0]["temperature"]["tmax"]
 hump = weather[0]["humidity"]
 #미세먼지 데이터
 dust = dust_data["weather"]["dust"]
 station = dust[0]["station"]["name"]#측정소 정보와 측정소 명이다
 dtime =dust[0]["timeObservation"] #관측시간을 나타냄
 value = dust[0]["pm10"]["value"] #미세먼지의 농도를 나타낸다
 grade = dust[0]["pm10"]["grade"] #미세먼지의 등급을 나타냄
 #오늘 강수량 데이터

 text ="지역기준:"+station+"\r\n----------\r\n오늘 날씨: "+sky+"\r\n"+"현재 온도: "+temp+"\r\n"+"최고 온도: "+tmax+"\r\n"
 text1 =text+ "미세먼지 수치: "+value +"\r\n "+"미세먼지 등급:"+grade+"\r\n\r\n"
 text1 =text+"상대습도:"+hump+"\r\n"+"강수량:"+precipitation+"\r\n----------\r\n"
 if float(precipitation)==0:
  text1=text1+"현재 기준으로 비가 오지 않네요 ㅎㅎ 외출을 하시는게 좋지 않을까요?\r\n 그리고 \r\n"
 elif float(precipitation)>0:
  text1=text1+"밖에 비가 오고 있네요 우산을 꼭 챙겨서 나가세요 \r\n 그리고 \r\n"
 if grade =='보통':
  message =text1+ "오늘 미세 먼지 등급이 보통이네요 \r\n 나가실때 마스크 끼고 나가세요~!"
  return message
 elif grade =='좋음':
  message =text1+ "미세 먼지 등급이 좋음!!! 마스크는 필요없을 것 같네요"
  return message
 elif grade =='매우나쁨'or grade =='약간나쁨'or grade=='나쁨':
  message =text1+ "미세먼지가 너무 많네요 외출을 자제하는게 좋지 않을까요??"
  return message
 else:
  return text1


def dust():
  params = {"version": "1", "lon":"128.5840","lat":"35.12454"} #딕셔너리 형식 - 사용하기 편리하다.

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

  text ="\r\n오늘 미세먼지 수치는 "+value+"이고, 등급은"+grade+"입니다."

  return text




def jason_data(text):

    dataSend = {
            "message": {
                "text": text
            }
        }
    return dataSend


app = Flask(__name__)


@app.route('/maps')
def maps():
 if area_1 ==" ":
  return redirect(url_for('fail'))
 else :
  return render_template('maps.html')

@app.route('/ajax')
def ajax():
 if area_1 ==" ":
  return redirect(url_for('fail')) 
 db = pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')
 cur =db.cursor()
 query = "select * from traf where area='"+area_1+"'"
 try: 
  cur.execute(query)
  rs=cur.fetchone()
  return jsonify(lat=rs[1],lon=rs[2])
 except:
  return redirect(url_for('fail'))

@app.route('/fail')
def fail():
 return render_template('fail.html')

@app.route('/')
def hello():

    return "hello"


@app.route('/keyboard',methods=['GET'])
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }
 
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']
    parse=re.sub('[ ]','',content)
    #print (parse)
    db = pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')
    cur = db.cursor()

    query = "select * from sttall where text1='"+parse+"'"
    try:
      cur.execute(query)
    except:
      dataSend = {
            "message":{
                "text": "무슨말인지 모르겠어요 다시한번 말씀해주세요!!"
            }
       }
      return jsonify(dataSend)
    rs = cur.fetchone()

    try:
      if content == u"시작하기":
         return jsonify(jason_data("주인장 블로그 : http://blog.naver.com/goldberg0408 \r\n -------------------- \r\n '도움말'을 입력해서 명령어들을 확인해보세요\r\n --------------------"))
      elif content == u"도움말":
         return jsonify(jason_data("교통정보 : 차가 막히는지 알 수 있습니다 \r\n 입력 예->교통정보 \r\n\r\n 날씨 : 해당 지역의 온도 날씨 미세먼지 값을 알 수 있습니다 \r\n 입력 예 ->날씨"))
      elif rs[0] =="날씨":
         text ="해당 명령어 목록 입니다 \r\n"
         cur.execute("select * from area") #지역 목록 개수를 파악하기 위한 구문
         data =cur.fetchall()
         for i in data:
          text = text+"-----지역이름:"+i[0]+"----\r\n"
          query = "select * from sttall where comm='weather' and text1 like '%"+i[0]+"%'"
          cur.execute(query)
          data_1=cur.fetchall();
          for t in data_1:
           text = text+t[0]+"\r\n"
         text = text+"\r\n위 명령어를 보내면 날씨 정보를 알 수 있습니다"
         return jsonify(jason_data(text))
      elif rs[1]=='weather':
         db.close()
         cur.close()
         try :

            return jsonify(jason_data(weather(rs[2])))
         except :
            return jsonify(jason_data(weather('부산')))
      elif rs[1]=='dust':
         return jsonify(jason_data(dust()))
      elif rs[1]=='교통':
         text ="해당 명령어 목록 입니다 \r\n\r\n"
         cur.execute("select * from area") #지역 목록 개수를 파악하기 위한 구문
         data =cur.fetchall()
         for i in data:
          text = text+"-----지역이름:"+i[0]+"----\r\n"
          query = "select * from sttall where area='"+i[0]+"'and comm='traf'"
          cur.execute(query)
          data_1=cur.fetchall();
          for t in data_1:
           text = text+t[0]+"\r\n"


         text = text + "\r\n 이렇게 한번 쳐보세요 \r\n ex)교통.동서고가"
         return jsonify(jason_data(text))
      elif rs[1]=='traf':
         split_data=rs[0].split('.')
         global area_1 
         area_1=split_data[1]
         return jsonify(jason_data("잠시만 기다려주세요~~~~!! \r\n http://115.40.151.150:5000/maps \r\n 이 주소를 클릭하세요!"));
      elif rs[1]=='call':
         return jsonify(jason_data("부르셨습니까??"))
      else:
         return jsonify(jason_data("무슨 말인지 모르겠습니다\r\n 다시한번 말씀해주세요 !"))
    except:
     return jsonify(jason_data("무슨 말인지 모르겠습니다.\r\n 다시 한번 말씀해주세요 !"))
    db.close()
    cur.close()
    return jsonify(dataSend)
 
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000,debug=True)
