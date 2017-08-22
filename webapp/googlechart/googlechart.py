from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import MySQLdb
import time


app = Flask(__name__)



def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
                raise RuntimeError('Not running with the Werkzeug Server')
        func()


@app.route('/shutdown')
def shutdown():
	try:
		db = MySQLdb.connect("localhost","root","1234","atmega128")
                cur = db.cursor()

                cur.execute("DELETE FROM ADC")
                db.commit()
                print "complete delete!!"
        except:
                print "fail!!"
        shutdown_server()
        return 'Server shutting down....'

@app.route('/')
def main():

        return render_template('google.html')

@app.route('/delete')
def delete():
	try:
		db = MySQLdb.connect("localhost","root","1234","atmega128")
		cur = db.cursor()

		cur.execute("DELETE FROM ADC")
		db.commit()
		db.close()
		cur.close()
		print "complete delte!!"

	except:
		print "fail !!"

	return render_template('google.html')


@app.route('/ajax')
def ajax():
	ch_0=[]
	ch_1=[]
	db =MySQLdb.connect("localhost","root","1234","atmega128")
	cur= db.cursor()
	cur.execute("select * from ADC")
	row = cur.fetchall()
	for i in row:
		ch_0.append(str(i[0]))
		ch_1.append(str(i[1]))
	db.close()
	cur.close()

	return jsonify(db_0=ch_0,db_1=ch_1)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8888,debug=True)


