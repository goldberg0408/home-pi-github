#coding: utf-8
import MySQLdb
from flask import Flask #u 플라스크 서버를 임포트 함
from flask import render_template
from flask import request


app = Flask(__name__)#u자기자신을 앱에 저장

def shutdown_server():#u서버를 닫는 함수 
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/shutdown')# https://192.168.1.163:8888/shutdown
def shutdown():
	shutdown_server()
	return 'Server shutting down...'


@app.route('/') #http://192.168.1.111:8888
def hello():
	db = MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	cur.execute("select * from EMP")
	row = cur.fetchall()

	templateData ={'data':row} #u row는 2차원 배열이다딕셔너리 
	return render_template('test2.html', **templateData)#html파일을 날림

	cur.close()
	db.close()
@app.route('/insert/<empno>,<ename>,<job>,<mgr>,<hiredate>,<sal>,<comm>')
def insert(empno,ename,job,mgr,hiredate,sal,comm):
	db = MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	cur.execute("insert into EMP(EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM) values('%s','%s','%s','%s','%s','%s','%s')" %(empno,ename,job,mgr,hiredate,sal,comm))
	db.commit()
	cur.execute("select * from EMP")
	row = cur.fetchall()
	templateData ={'data':row}
	return render_template('insert.html', **templateData)

	cur.close()
	db.close()
@app.route('/insert')
def insert_1():
	db=MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	cur.execute("select * from EMP")
	row = cur.fetchall()
	templateData ={'data':row}
	return render_template('insert.html', **templateData)

	cur.close()
	db.close()
@app.route('/delete/<ename>')
def delete(ename):
	db=MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	cur.execute("delete from EMP where ENAME='%s'" %(ename))
	db.commit()
	cur.execute("select * from EMP")
	row = cur.fetchall()
	templateData ={'data':row}
	return render_template('delete.html',**templateData)

	cur.close()
	db.close()
@app.route('/create')
def create():
	db = MySQLdb.connect("localhost","root","1234","SCOTT")
	cur = db.cursor()
	try:
		cur.execute("create table persons(ID int,name varchar(255),address varchar(255));")
		db.commit()
	except:
		return "exist table!!!!!"

	cur.execute("select * from persons")
	row = cur.fetchall()
	templateData ={'data':row}
	return render_template('create.html',**templateData)

	cur.close()
	db.close()
@app.route('/DROP')
def DROP():
	db = MySQLdb.connect("localhost","root","1234","SCOTT")
	cur= db.cursor()
	cur.execute("DROP table persons;")
	return "complete drop table"
	
if __name__ == "__main__": #u 자신의 main을 구분 하기 위해
	app.run(host='0.0.0.0',port=8888,debug=True)
