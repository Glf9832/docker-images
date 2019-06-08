from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from flask import Flask

broker = 'amqp://guest:guest@{0}:{1}'.format(
    os.environ.get('RABBIT_HOST'),
    os.environ.get('RABBIT_PORT')
)

celery_app = Celery('tasks', broker=broker)


@celery_app.task()
def add(x, y):
    return x + y

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>首页</h1>'

@app.route('/api')
def api():
    return '<h1>API测试</h1>'

@app.route('/task1')
def task1():
    task = add.delay(1, 2)
    return '<h1>%s</h1>' % task.id

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
