# -*- coding: utf-8 -*
import pymysql

db = pymysql.connect(host="localhost",user="root",passwd="1234",db="stt",charset='utf8')
cur =db.cursor()

list=cur.execute("select distinct area from sttall where comm='traf'")

cur.execute("select * from area")
data =cur.fetchall()

for i in data:
 print (i[0])
 query = "select * from sttall where area='"+i[0]+"'and comm='traf'"
 cur.execute(query)
 data_1=cur.fetchall();
 for i in data_1:
       print (i[0])


#print (cur.execute("select distinct area from sttall where comm='traf'"))

