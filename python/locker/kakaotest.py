# -*- coding: utf-8 -*-
 
import os
from flask import Flask, request, jsonify

#소켓 라이브러리
import socket 
#데이터베이스 라이브러리
import pymysql
def jason_data(text):

    dataSend = {
            "message": {
                "text": text
            }
        }
    return dataSend

 
 
app = Flask(__name__)
 
 
 
@app.route('/keyboard')
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }
 
    return jsonify(dataSend)
 
@app.route('/find',methods=['POST']) #찾기 경로
def find():

    #ip_addr = request.form.get('ip_addr')
    #port = request.form.get('port')
    key_value = request.form.get('key_value')
    #comm = request.form.get('comm')
    #클라이언트로부터 db에 있는 데이터인지 검증받기 위해 데이터를 받음
    db= pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem",charset="utf8")
    cur = db.cursor()
    query = "select * from m_info where sec_key='"+key_value+"'"
    try: #넘겨 받은 데이터가 있는지 한번 확인하는것
       cur.execute(query)
       rs =cur.fetchone()
       datasend = { "verify":"OK",
                 "comm":rs[9] }
       print (rs)
       return jsonify(datasend)

    except:
       datasend ={"verify":"FAIL"}
       return jsonify(datasend)

@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']

    db = pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem",charset="utf8")
    cur = db.cursor()
    #인증키와 같은 행을 찾아서 출력
    query = "select * from m_info where sec_key='"+content+"'"
    cur.execute(query)
    rs =cur.fetchone()
    print (rs)
    if content == u"시작하기":
        return jsonify(jason_data("안뇽"))
    elif content == u"도움말":
        return jsonify(jason_data("도움말"))
    elif content == rs[5]:
      try:
        print("연결대기중")
        s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((rs[0],rs[1])) #넘겨받은 데이터로  소켓서버,포트 생성
        s.listen(1)
        conn,addr = s.accept() # 해당 라우트로 오면 해당 포트를 가진 소켓 클라이언트$
        print ("소켓 서버에 연결한 ip :" ,addr)
        text =rs[9] #데이터베이스 command 컬럼
        conn.send(text.encode()) # 해당 ip로 데이터를 보냄
        conn.close()
        s.close()
        del s #객체 삭제
        return jsonify(jason_data("이용해 주셔서 감사합니다."))
      except :
        return jsonify(jason_data("다시한번 시도해주세요"))

    else :
        return jsonify(jason_data("실패"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000,debug=True)
