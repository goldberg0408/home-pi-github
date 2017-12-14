# -*- coding: utf-8 -*-
 
import os
from flask import Flask, request, jsonify

#소켓 라이브러리
import socket 
#데이터베이스 라이브러리
import pymysql
#스레드,큐
import threading
import queue
import time
#sms 라이브러리
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
import sys

api_key = "NCS76REGORDXIHMI"
api_secret = "XSCPKTB0CVFBVWBMHV1QNLM7IG2KL2XB"
cool = Message(api_key,api_secret)

queue =queue.Queue() #소켓서버 결과값을 반환하기위한 큐
#queue1 =queue.Queue() #소켓서버 결과값을 반환하기위한 큐

socket_lock = threading.Lock()
def jason_data(text):

    dataSend = {
            "message": {
                "text": text
            }
        }
    return dataSend

def sms_thread(location,name,sec_key,phone):
    # set api key, api secret
    #api_key = "NCS76REGORDXIHMI"
    #api_secret = "XSCPKTB0CVFBVWBMHV1QNLM7IG2KL2XB"

    text = "지역:"+location+"\r\n"+name+"고객님의 인증키는 \r\n"+sec_key+"\r\n입니다"
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = phone # Recipients Number '01000000000,01000000001'
    params['from'] = '01066592209' # Sender number
    params['text'] = text # Message

    try:
        response = cool.send(params)
        #print("Success Count : %s" % response['success_count'])
        #print("Error Count : %s" % response['error_count'])
        #print("Group ID : %s" % response['group_id'])

        #if "error_list" in response:
           # print("Error List : %s" % response['error_list'])
        queue.put("OK")
    except CoolsmsException as e:
        #print("Error Code : %s" % e.code)
        #print("Error Message : %s" % e.msg)
        queue.put("FAIL")

    sys.exit()



def socket_connect(ip,port,comm,location,name): #소켓 쓰레드
  start_time=time.time()
  print("연결대기중")
  s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((ip,port)) #넘겨받은 데이터로  소켓서버,포트 생성
  s.settimeout(0.09)
  s.listen(1)
  try:
   conn,addr = s.accept() # 해당 라우트로 오면 해당 포트를 가진 소켓 클라이언트$
   socket_lock.acquire()
   print ("소켓 서버에 연결한 ip :" ,addr)
   text =comm #데이터베이스 command 컬럼
   conn.send(text.encode()) # 해당 ip로 데이터를 보냄
   socket_lock.release()
   test="지역:"+location+"\r\n"+name+"고객님 이용해 주셔서 감사합니다. \r\n"
   queue.put(test) # 결과 값을 큐에 데이터를 집어 넣음
   print ("%s" %(time.time()-start_time))
  except:
   test= "서버와의 접속이 원활하지 않습니다.\r\n 다시한번 시도해주세요 "
   queue.put(test) #예외가 발생 했을 때 카카오톡으로 오류를 반환하기 위해 큐에 데이터를 집어넣음
   pass
  finally:
   del s
   del start_time
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

    location = request.form.get('location')
    name = request.form.get('name')
    sec_key = request.form.get('sec_key')
    phone = request.form.get('phone')
    #box_num = request.form.get('box_num')

    t2 = threading.Thread(target =sms_thread ,args=(location,name,sec_key,phone))
    t2.start()
    result =queue.get()
    print (result)
    #try: #넘겨 받은 데이터가 있는지 한번 확인하는것
       #cur.execute(query)
       #rs =cur.fetchone()
       #datasend = { "verify":"OK",
       #          "comm":rs[8] } # 명령어를 보내는 문구
       #print (rs)
       #return jsonify(datasend)

    #except:
      # datasend ={"verify":"FAIL"}
      # return jsonify(datasend)
   
    datasend = {"verify":result}
    return jsonify(datasend)
@app.route('/message', methods=['POST'])
def Message():

   dataReceive = request.get_json()
   content = dataReceive['content']
   try:
     db = pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem",charset="utf8")
     cur = db.cursor()
      #인증키와 같은 행을 찾아서 출력
     query = "select * from m_info where sec_key='"+content+"'"
     cur.execute(query)
     rs =cur.fetchone()
     #rs =cur.fetchone()
     print (rs)
     if content == u"시작하기":
       return jsonify(jason_data("주의 !!\r\n 인증키를 입력했을 때, \r\n 고객님의 사물함이 바로 열립니다.\r\n 사물함 앞에서 인증키를 인증하세요"))
     elif content == u"도움말":
       return jsonify(jason_data("도움말"))
     elif content == rs[5]:
       t1 =threading.Thread(target=socket_connect,args=(rs[0],rs[1],rs[7],rs[2],rs[3]))
       t1.start() #쓰레드에 파라메터 값을 넘기고 쓰레드를 시작
       #test = queue.get() #큐에 데이터가 들어갔고 그 값을 받을 떄까지는 get 함수는 block 상태
       #print ("카카오톡 : ",test)
       try:
        text ="지역:"+rs[2]+"\r\n"+rs[3]+" 고객님 \r\n 이용해 주셔서 감사합니다."
        return jsonify(jason_data(text))
       except :
        return jsonify(jason_data("다시한번 시도해주세요"))
   except:
     print ("db접속실패")
     return jsonify(jason_data("고객님의 정보가 존재하지 않습니다."))


if __name__ == "__main__" :
    app.run(host='0.0.0.0', port = 5000,debug=True)
