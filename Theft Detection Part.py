import RPi.GPIO as GPIO
import time
import requests
import picamera
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)        
GPIO.setup(27, GPIO.OUT)
k=0
while True:
    i=GPIO.input(17)
    if i==0:                 
        print("No intruders",i)
        GPIO.output(27, 0)  
        time.sleep(0.1)
    elif i==1:               
        print("Intruder detected",i)
        GPIO.output(27, 1)
        k=str(k)
        n="/home/pi/Desktop/intruder_pics/intruder"+k+".jpg"
        camera=picamera.PiCamera()
        camera.capture(n)
        requests.post(url='https://maker.ifttt.com/trigger/my_theft_sensor/with/key/bn9mSvndGLXCpw-O7UCciD')
        time.sleep(2.5)
        k=int(k)
        k=k+1
        camera.close()
        
