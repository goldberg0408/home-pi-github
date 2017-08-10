from flask import Flask
from flask import render_template
from flask import request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

leds = {
    24 : {'name':'LED','state':GPIO.LOW},
    3  : {'name':'LED','state':GPIO.LOW} 
}

for led in leds :
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)

def getGpioState():
    for led in leds :
        leds[led]['state'] = GPIO.input(led)
    return leds

@app.route("/")
def main():
    gpioState = {
        'leds' : getGpioState()
    }
    return render_template('main.html',**gpioState)

@app.route("/<led>/<act>")
def action(led,act):
    led =int(led)
    leds=getGpioState()
    dev =leds[led]['name']

    if act =="on":
        GPIO.output(led,GPIO.HIGH)
        msg = "truned" +dev+"on"
    elif act == "off":
        GPIO.output(led,GPIO.LOW)
        msg ="turned"+ dev + "off"
    else:
        msg = "Undefined action!"

    gpioState ={
        'msg' : msg,
        'leds' : getGpioState()
        }
    return render_template('main.html',**gpioState)

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=8888,debug=True)
