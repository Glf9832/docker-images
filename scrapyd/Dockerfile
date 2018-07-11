FROM sshd:ubuntu

ADD ./requirements.txt /opt
RUN virtualenv -p /usr/bin/python3 /opt/venv3 \
    && /opt/venv3/bin/pip install -r /opt/requirements.txt

ADD ./default_scrapyd.conf /opt/venv3/lib/python3.5/site-packages/scrapyd

# CMD ["/opt/venv3/bin/scrapyd"]

ENTRYPOINT ["/opt/venv3/bin/scrapyd"]
