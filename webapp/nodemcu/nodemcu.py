from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import json
import time
import MySQLdb


base_url ="http://192.168.1.141:8888"
events_url = base_url + "/events"




app = Flask(__name__)

def shutdown_server():
	func = request.eviron.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')

	func()



@app.route('/')
def main():
	return render_template('nodemcu.html')

@app.route('/ajax')
def ajax():
	temp=[]
	humi=[]
	global lat
	global lng
	db = MySQLdb.connect("localhost","root","1234","DHT11")
	cur=db.cursor()
	cur.execute("select * from DHT_11")

	row = cur.fetchall()
	for i in row:
		temp.append(str(i[0]))
		humi.append(str(i[1]))
		lat =i[0]
		lng =i[1]
	
	db.close()
	cur.close()
	return jsonify(db_0=temp,db_1=humi)
@app.route('/ajax_1')
def ajax_1():
	ch_0=[]
	ch_1=[]
	global zoom
	db = MySQLdb.connect("localhost","root","1234","atmega128")
	cur = db.cursor()
	cur.execute("select * from ADC")
	row = cur.fetchall()
	for i in row:
		ch_0.append(str(i[0]))
		ch_1.append(str(i[1]))
                zoom=i[0]
	if zoom>8:
		zoom=8;
	db.close()
	cur.close()
	
	return jsonify(c_0=ch_0,c_1=ch_1)
@app.route('/map')
def map():
	print (lat)
	print (lng)
	print (zoom)
	return jsonify(lt=lat,lg=lng,zm=zoom)

@app.route('/delete')
def delete():
        try:
                db = MySQLdb.connect("localhost","root","1234","DHT11")
                cur = db.cursor()
		db1 = MySQLdb.connect("localhost","root","1234","atmega128")
		cur1 =db1.cursor()

		cur1.execute("DELETE FROM ADC")
                cur.execute("DELETE FROM DHT_11")

		db1.commit()
                db.commit()

		db1.close()
                db.close()
		cur1.close()
                cur.close()
                print "complete delte!!"

        except:
                print "fail !!"

        return render_template('nodemcu.html')




if __name__ == "__main__":
	app.run(host ='0.0.0.0',port=8888,debug=True)
