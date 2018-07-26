FROM greene/python3:centos7

USER root

WORKDIR /opt

ADD requirements.txt /opt

RUN curl https://files.pythonhosted.org/packages/12/2a/e9e4fb2e6b2f7a75577e0614926819a472934b0b85f205ba5d5d2add54d0/Twisted-18.4.0.tar.bz2 -o /opt/Twisted-18.4.0.tar.bz2 --progress \
    && tar -xvf Twisted-18.4.0.tar.bz2 -C /opt

WORKDIR /opt/Twisted-18.4.0

RUN /opt/venv3/bin/python3 setup.py install

WORKDIR /opt

RUN /opt/venv3/bin/pip install -r /opt/requirements.txt \
    && rm -rf /opt/Twisted-18.4.0  /opt/Twisted-18.4.0.tar.bz2

WORKDIR /opt/SSM

ENTRYPOINT ["bash"]
CMD ["startservice.sh"]

EXPOSE 8000
