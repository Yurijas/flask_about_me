from app import app
from flask import render_template, url_for, redirect

@app.route('/')
@app.route('/index')
@app.route('/index/<flag>', methods=['GET'])
def index(flag='True'):
    hobbies = ['Hula-hoop', 'Pokemon Go']
    return render_template('index.html', title='HOME', hobbies=hobbies, flag=flag)

@app.route('/data')
@app.route('/data/<name>', methods=['GET'])
def data(name='Yurie Seijas', description = 'I am learning Python. I have studied HTML, CSS and JavaScript before. My mejor at my college in Japan was Spanish.'):
    return render_template('data.html', name=name, description=description, title='Data')
