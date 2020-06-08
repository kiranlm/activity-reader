FROM python:latest

MAINTAINER Kiran LM "kiran.lm96@gmail.com"

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt
COPY ./app/app.py /app.py
COPY ./data /data


RUN pip install -r /requirements.txt

EXPOSE $BIND_PORT

ENTRYPOINT [ "python" ]

CMD ["/app.py"]