from socket import *
#*-* coding: utf-8*-*

s = socket(AF_INET,SOCK_STREAM)
s.bind(("",8000))
s.listen(1)

print 'coneect waiting...'

conn,addr = s.accept()
while 1:
	data =conn.recv(1024)
	if not data:
		break
	print 'recive_data:',data
     	conn.send(data)
conn.close()
s.close()
