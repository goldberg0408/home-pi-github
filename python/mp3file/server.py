from socket import *
from flask import Flask
#*-* coding: utf-8*-*

app = Flask(__name__)



s = socket(AF_INET,SOCK_STREAM)
s.bind(("0.0.0.0",5000)) #포트 5000으로 소켓서버 생성
s.listen(1)



@app.route('/')
def hello():
 print ("연결 대기중..")
 conn,addr = s.accept() # 해당 라우트로 오면 소켓 클라이언트의 접속을 대기
 print ("소켓 서버에 연결한 ip :" ,addr)
 text ="led:1\r"
 conn.send(text.encode()) # 해당 ip로 데이터를 보냄
 conn.close()
 return 'seccess'

if __name__ =='__main__':
 app.run(host='0.0.0.0',port=5001) #포트 5001로 플라스크 서버 생성
