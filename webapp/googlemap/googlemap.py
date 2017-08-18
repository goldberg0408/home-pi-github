# -*- coding: utf-8 -*
from flask import Flask
from flask import render_template
from flask import request
import serial
import json
import requests
import time

app = Flask(__name__)

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('not running')
	func()


@app.route('/shutdown')
def shutdown():
	shutdown_server()
	return 'sever shut down'

@app.route('/')
def main():
	lat =input("위도룰 입력하세요")
        lng =input("경도를 입력하세요")
        zoom=input("몇배 확대 할 것인가요?")
	
	params = {"version": "1", "lon":lng,"lat":lat}
	headers = {"appKey": "b81288c9-41ec-3d16-90bd-a8b4784730a5"}

	r = requests.get("http://apis.skplanetx.com/weather/dust", params=params, headers=headers)

	data =json.loads(r.text)
	weather =data["weather"]["dust"]
	dtime	=weather[0]["timeObservation"]
	value	=weather[0]["pm10"]["value"]
	grade	=weather[0]["pm10"]["grade"]

	templatedata = {'lat':lat ,'lng':lng,'zoom':zoom,'value':value,'grade':grade}

	return render_template('google.html', **templatedata)



if __name__ =="__main__":

	app.run(host ='0.0.0.0',port=8888,debug=True)
