# -*- coding: utf-8 -* 
import pymysql

db=pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')

query = "select * from sttall where text1='야'"
cur=db.cursor()
cur.execute(query)
rs = cur.fetchone()

print (rs)
print
