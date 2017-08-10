from flask import Flask
from flask import render_template
from flask import request
import serial
import MySQLdb

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
	while 1:
		db =MySQLdb.connect("localhost","root","1234","atmega128")
		cur= db.cursor()
		
		ser = serial.Serial('/dev/ttyUSB0',9600)
		ser.close()
		ser.open()
		response = ser.readline()
		ser.close()

		split_data=response.split(',')
		print split_data[0]
		print split_data[1]
		cur.execute("insert into ADC(ch_1,ch_2) values('%s','%s')" %(split_data[0],split_data[1]))
		db.commit()
		cur.execute("select * from ADC")
		row =cur.fetchall()
		templateData = {'data':row}
		cur.close()
		db.close()
		return render_template('adc.html', **templateData)



if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8888,debug=True)
