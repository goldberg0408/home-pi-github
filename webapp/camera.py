import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)


with picamera.PiCamera() as picam:
        picam.start_preview()
        GPIO.wait_for_edge(24, GPIO.FALLING)
        picam.capture('/home/pi/img.jpg')
        picam.stop_preview()
