# coding : utf-8
import MySQLdb
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

def shutdown_server():
	func =request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running')
	func()

@app.route('/shutdown')
def shutdown():
	shutdown_server()
	return 'server shutting down..'

@app.route('/account',methods=['POST'])
def account():

	return render_template('account.html')

@app.route('/join',methods=['POST'])
def join():
	id = request.form['ID']
	password = request.form['PASSWORD']
	db = MySQLdb.connect("localhost","root","1234","MEMBER")
	cur=db.cursor()
	cur.execute("insert into idandpass(personID,password) values('%s','%s')" %(id,password))
	db.commit()
	return render_template('form_test.html')
@app.route('/mainpage',methods =['POST'])
def mainpage():
	id = request.form['ID']
	password = request.form['pass']

	db = MySQLdb.connect("localhost","root","1234","MEMBER")
	cur= db.cursor()
	
	try:
		cur.execute("select personID from idandpass where personID='%s'" %(id))
		recent_id=cur.fetchone()
		list(recent_id)
	except:
		return render_template('form_test.html')
	
	try:	
		cur.execute("select password from idandpass where password=%s" %(password))
		recent_password=cur.fetchone()
		list(recent_password)
	except:
		return render_template('form_test.html')
	
	cur.close()
	db.close()
	
	if((id==str(recent_id[0])) and(str(password) ==str(recent_password[0]) ) ):
		database = MySQLdb.connect("localhost","root","1234","SCOTT")
		db_cur=database.cursor()
		db_cur.execute("select * from EMP")
		database.commit()
		db_data=db_cur.fetchall()
		template_db = {'data':db_data}
		return render_template('form_test2.html',**template_db)
	else:
		return render_template('form_test.html')

@app.route('/')
def root():
	return render_template('form_test.html')


if __name__ =="__main__":
	app.run(host='0.0.0.0', port=8888, debug=True)
