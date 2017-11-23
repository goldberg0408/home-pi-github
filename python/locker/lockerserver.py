# -*- coding: utf-8 -*-
#파이썬3에서 동작합니다.
import os
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import abort,redirect,url_for


app = Flask(__name__)

@app.route('/post', methods=['POST'])
def message():
 data =request.form.get('text')
 data1 =request.form.get('call')

 print (data)
 print (data1)
 datasend = {'text':'hello','call':'what?'}

 return jsonify(datasend)


@app.route('/')
def hello():

 return "hello"

if __name__ == "__main__":
 app.run(host='0.0.0.0')
