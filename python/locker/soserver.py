#*-* coding: utf-8*-*
import socket
from flask import Flask

app = Flask(__name__)

@app.route('/<int:port>,<data>')
def hello(port,data):
  print ("연결 대기중..")
  s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind(("",port)) #넘겨받은 데이터로  소켓서버,포트 생성
  s.listen(1)
  conn,addr = s.accept() # 해당 라우트로 오면 해당 포트를 가진 소켓 클라이언트의 접속을 대기
  print ("소켓 서버에 연결한 ip :" ,addr)
  text =data
  conn.send(text.encode()) # 해당 ip로 데이터를 보냄
  conn.close()
  s.close()
  del s #객체 삭제

  return '소켓서버포트:'+str(port)

if __name__ =='__main__':
 app.run(host='0.0.0.0',port=5000) #포트 5001로 플라스크 서버 생성

