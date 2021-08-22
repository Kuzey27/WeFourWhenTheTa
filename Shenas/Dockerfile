FROM ubuntu:18.04

RUN apt-get update --fix-missing && \
    apt-get upgrade -y && \
    apt-get -y install tzdata && \
    ln -sf /usr/share/zoneinfo/UTC /etc/localtime
RUN apt-get install -y git --fix-missing
RUN dpkg-reconfigure -f noninteractive tzdata

ENV PYTHONIOENCODING=utf-8

RUN apt-get install -y gcc python3 python3-pip netcat openssl libssl-dev libpq-dev vim gettext --fix-missing

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install -U pip

ADD requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt

ADD . /usr/shenas
WORKDIR /usr/shenas/

ARG DEBUG

ENTRYPOINT ["bash", "docker-entrypoint.sh"]
