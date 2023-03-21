FROM python:3.11.2

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY app.py entrypoint.sh ./

ENV ENV=docker-desktop
ENV FEATURES=some,dev,features
ENV PORT=80
ENV ADDRESS=0.0.0.0

ENTRYPOINT ["/app/entrypoint.sh"]
