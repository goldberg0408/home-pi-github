from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('ajax.html')

@app.route('/ajax')
def add_numbers():
    result ="ajax.test"	
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)
