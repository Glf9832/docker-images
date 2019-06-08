
FROM cnas-base:latest

WORKDIR /cloud_cnas_project

COPY ./app.py ./app.py
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

RUN chmod +x docker-entrypoint.sh

ENV WEB_PORT 8000
EXPOSE $WEB_PORT

ENTRYPOINT ["./docker-entrypoint.sh"]
