from __future__ import absolute_import, unicode_literals

from celery import Celery

from .config import Config

app = Celery(__name__)
app.config_from_object(Config)

@app.task()
def add_async(x, y):
    return x + y


@app.task()
def schedule_async():
    return 'this is a schedule task.'
