from flask import Flask
from flask import render_template
from flask import request
import serial

app = Flask(__name__)

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/shutdown')
def shutdown():
	shutdown_server()
	return 'Server shutting down....'

@app.route('/')
def main():
	while 1:
		ser = serial.Serial('/dev/ttyUSB0',9600)
		ser.close()
		ser.open()
		response = ser.readline()
		ser.close()

		split_data=response.split(',')
	
		templateData = {'data':split_data}
		return render_template('adc.html', **templateData)



if __name__ == "__main__":
	app.run(host='0.0.0.0',port=8888,debug=True)
