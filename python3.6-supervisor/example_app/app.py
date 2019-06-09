from flask import Flask
from .task import add_async

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>首页</h1>'

@app.route('/api')
def api():
    return '<h1>API测试</h1>'

@app.route('/task1')
def task1():
    task = add_async.delay(1, 2)
    return '<h1>%s</h1>' % task.id
