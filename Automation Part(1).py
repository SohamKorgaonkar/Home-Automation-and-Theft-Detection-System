from flask import Flask, request
import gpiozero
import RPi.GPIO as g
import string
import requests


#defines the number of relay pins
relay_1=14
relay_2=18

#sets warnings to false and pin numbering mode to broadcom
g.setwarnings(False)
g.setmode(g.BCM)
g.setup(14,g.OUT)
g.setup(18,g.OUT)

#creates a function to trigger relay 1 and 2
def relay_trigger(a,b):
    relay_1=14
    relay_2=18
    if(a==1):
        if(b==1):
            g.output(relay_1,g.HIGH)
        elif(b==0):
            g.output(relay_1,g.LOW)
    elif(a==2):
        if(b==1):
            g.output(relay_2,g.HIGH)
        elif(b==0):
            g.output(relay_2,g.LOW)

#pin 4 is used for PWM LED
g.setup(4,g.OUT)
#sets PWM Frequency of pin 4 to 200Hz
p=g.PWM(4,200)


 
app = Flask(__name__)
    
#syntax to create a flask listner server
 
@app.route('/', methods = ["POST"])
def post():
    c=request.data.decode()
    print(c)
    if(c=='led on'):
        p.start(100)
    elif(c=='led off'):
        p.start(0)
    elif(c.isdigit()):
        p.start(int(c))
    elif(c=='r_on_1'):
        relay_trigger(1,1)
    elif(c=='r_down_1'):
        relay_trigger(1,0)
    elif(c=='r_on_2'):
        relay_trigger(2,1)
    elif(c=='r_down_2'):
        relay_trigger(2,0)
    elif(c=='room on'):
        requests.get('http://192.168.1.104/LED=ON')
    elif(c=='room off'):
        requests.get('http://192.168.1.104/LED=OFF')
    elif(c=='room high'):
        requests.get('http://192.168.1.104/LED=HIGH')
    elif(c=='room medium'):
        requests.get('http://192.168.1.104/LED=MEDIUM')
    elif(c=='room low'):
        requests.get('http://192.168.1.104/LED=LOW')
    return ''
 
app.run(host='0.0.0.0', port= 38212)
