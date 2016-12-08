FROM python:3.6-rc

RUN mkdir -p /app
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 app.py
