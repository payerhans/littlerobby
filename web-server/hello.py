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
    template_data = {
        'direction' : 'left'
    }
    return render_template('main.html', **template_data)

@app.route('/right')
def right():
    template_data = {
        'direction' : 'right'
    }
    return render_template('main.html', **template_data)

@app.route('/forward')
def forward():
    robby.forward()
    sleep(1)
    robby.stop()
    return 'true'

@app.route('/backward')
def backward():
    template_data = {
        'direction' : 'backward'
    }
    return render_template('main.html', **template_data)

@app.route('/stop')
def stop():
    template_data = {
        'direction' : 'stopped'
    }
    return render_template('main.html', **template_data)

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)
    #app.run(debug = True)
