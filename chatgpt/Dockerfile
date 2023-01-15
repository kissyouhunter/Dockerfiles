FROM python:3.10.8-alpine3.16

ADD ./ /app

RUN rm -f Dockerfile \
    && pip install openai \
    && pip install pyTelegramBotAPI \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >  /etc/timezone

WORKDIR /app

ENTRYPOINT python -u chat.py
