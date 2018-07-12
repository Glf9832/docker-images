FROM docker.io/centos:latest

RUN yum install -y gcc make openssl openssl-devel sqlite-devel bzip2 \
    && curl https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz -o /opt/Python-3.6.5.tar.xz --progress \
    && tar -xvf /opt/Python-3.6.5.tar.xz -C /opt \
    && mkdir /opt/python3.6

WORKDIR /opt/Python-3.6.5

RUN ./configure --prefix=/opt/python3.6

ADD ./Setup /opt/Python-3.6.5/Modules/

WORKDIR /opt/Python-3.6.5

RUN make \
    && make install \
    && /opt/python3.6/bin/pip3 install virtualenv \
    && /opt/python3.6/bin/virtualenv -p /opt/python3.6/bin/python3 /opt/venv3 \
    && rm -rf /opt/Python-3.6.5  /opt/Python-3.6.5.tar.xz

WORKDIR /opt/
