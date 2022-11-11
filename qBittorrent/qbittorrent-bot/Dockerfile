FROM python:3.10.8-alpine3.16
ADD . /app
RUN apk add --no-cache build-base linux-headers \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >  /etc/timezone \
    && cp -f /app/config.example.toml /app/config.toml \
    && mkdir -p /Downloads \
    && cd /app && pip3 install -r requirements.txt
WORKDIR /app
ENTRYPOINT python main.py
