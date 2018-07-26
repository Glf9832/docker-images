#!/usr/bin/env bash
nohup /opt/venv3/bin/celery -B -A schedule.celery_app worker -l info &
/opt/venv3/bin/python /opt/SSM/manage.py runserver 0.0.0.0:8000