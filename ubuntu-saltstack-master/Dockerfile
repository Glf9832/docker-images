FROM docker.io/ubuntu:18.04

USER root

WORKDIR /opt

RUN apt-get update \
    && apt-get install salt-master -y

ADD master /etc/salt

WORKDIR /etc/init.d

ENTRYPOINT ["salt-master"]
CMD ["start"]
