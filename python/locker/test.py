# -*- coding: utf-8 -*
import serial
import pymysql

db = pymysql.connect(host="192.168.1.180",user="client",passwd="1234",db="lockersystem")
cur = db.cursor()

cur.execute("select * from lockerlocation")
rs = cur.fetchall()

print (rs)
