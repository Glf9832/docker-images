FROM docker.io/ubuntu:18.04

USER root

WORKDIR /opt

RUN apt-get update \
    && apt-get install salt-minion -y

ADD minion /etc/salt

WORKDIR /etc/init.d

ENTRYPOINT ["salt-minion"]
CMD ["start"]
