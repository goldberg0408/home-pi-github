import smtplib
from email.mime.text import MIMEText

me = 'goldberg0408@gmail.com'
you = 'goldberg0408@naver.com'
contents = 'this is linux'

msg = MIMEText(contents, _charset='euc-kr')

msg['subject'] = 'Hello'
msg['from'] = me
msg['To'] = you

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('goldberg0408@gmail.com','skduddl1')


server.sendmail(me,you,msg.as_string())
print('succes send mail')
server.quit()
