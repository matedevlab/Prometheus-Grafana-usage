FROM python:3.9-slim

WORKDIR /app

COPY app.py requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py" ]

EXPOSE 5000
