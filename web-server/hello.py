from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    template_data = { 
            'header': 'Hello World!',
            'text' : 'Hallo Mario'
            }
    return render_template('main.html', **template_data)

if __name__ == '__main__':
    app.run('0.0.0.0', debug = True)
    #app.run(debug = True)
