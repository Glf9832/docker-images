#!/usr/bin/env bash

set -e

source "/cloud_cnas_project/tmenv/bin/activate"

case $1 in
    flask)
    gunicorn app:app -b 0.0.0.0:$WEB_PORT;;

    worker)
    celery -A app.celery_app worker -l info;;
esac

exec "$@"
