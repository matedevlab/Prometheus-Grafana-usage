FROM python:3.9-alpine3.17

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip3 install -r requirements.txt

CMD python3 app.py

EXPOSE 5000