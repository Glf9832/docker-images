FROM python:v3.6

USER root

RUN yum -y install openssh-server

ADD ./sshd_config /etc/ssh/

RUN ssh-keygen -q -t rsa -b 2048 -f /etc/ssh/ssh_host_rsa_key -N '' \
    && ssh-keygen -q -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N '' \
    && ssh-keygen -t dsa -f /etc/ssh/ssh_host_ed25519_key -N '' \
    && echo root:123456|chpasswd

ENTRYPOINT ["/usr/sbin/sshd"]

CMD ["-D"]

