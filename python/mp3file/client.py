#*-* coding: utf-8 *-*
from socket import *
HOST='192.168.1.179'
c = socket(AF_INET, SOCK_STREAM)
print 'connecting....'
c.connect((HOST,8000))
print 'ok'
while 1:
        data = raw_input()
        if data:
                c.send(data)
        else:
                continue
        print 'recive_data : ',c.recv(1024)
c.close()
