# coding:utf-8
import smtplib
from email.mime.text import MIMEText

me =input("자신의 이메일 주소를 입력하세요 (구글 이메일 계정)")
password =input("자신의 이메일 주소의 비밀번호를 입력하세요")
you =input("상대방의 이메일 주소를 입력하세요")
subject = input("제목을 입력하세요")
contents =input("내용을 입력하세요")

msg =MIMEText(contents, _charset='euc-kr')


msg['subject']= subject
msg['from']=me
msg['To']=you

server = smtplib.SMTP('SMTP.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(me,password)

try:
	server.sendmail(me,you,msg.as_string())
	print ("메일보내기 성공!")

except:
	print("메일 보내기 실패 ")

server.quit()

