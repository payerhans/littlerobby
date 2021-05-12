from flask import Flask, render_template, request
from gpiozero import Robot
from time import sleep
import os

app = Flask(__name__)

template_data = {'status' : 'Robby wartet auf initialisierung '}

try:
    robby = Robot(left=(20, 21), right=(12, 16))
    template_data = {
        'status' : 'Robby bereit'
    }
except:
    template_data = {
        'status' : 'Robby nicht bereit, etwas ist schiefgegeangen'
    }



@app.route('/')
def hello_world():
    """ template_data = { 
            'header': 'Hello World!',
            'text' : 'Hallo Mario'
            } """
    return render_template('main.html', **template_data)

@app.route('/left')
def left():
    robby.left()
    return 'true'

@app.route('/right')
def right():
    robby.right()
    return 'true'

@app.route('/forward')
def forward():
    robby.forward()
    return 'true'

@app.route('/backward')
def backward():
    robby.backward()
    return 'true'

@app.route('/stop')
def stop():
    robby.stop()
    return 'true'

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)
    #app.run(debug = True)
