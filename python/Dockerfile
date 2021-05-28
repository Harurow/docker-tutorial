FROM python:3.9.0-slim-buster

WORKDIR /sandbox

RUN pip install mysql-connector-python

ADD --chmod=755 hello-world.py /usr/local/

CMD [ "/usr/local/hello-world.py" ]
