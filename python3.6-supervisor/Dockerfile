
FROM cnas-base:latest

WORKDIR ${APP_HOME}

COPY ./example_app ./example_app
COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

RUN chmod +x docker-entrypoint.sh

ENV WEB_PORT 8000
# ENV RABBIT_HOST rabbitmq
# ENV RABBIT_PORT 5672
ENV REDIS_HOST redis
ENV REDIS_PORT 6379
ENV REDBEAT_DB 0
ENV BROKER_DB 0
ENV RESULT_DB 0

EXPOSE $WEB_PORT

ENTRYPOINT ["./docker-entrypoint.sh"]
