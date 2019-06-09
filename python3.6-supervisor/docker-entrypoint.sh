#!/usr/bin/env bash

set -e

source "/cloud_cnas_project/tmenv/bin/activate"

case $1 in
    flask)
    gunicorn example_app.app:app -b 0.0.0.0:$WEB_PORT;;

    worker)
    celery -A example_app.task worker -l info;;

    beat)
    celery beat -A example_app.task -l info;;
esac

exec "$@"
