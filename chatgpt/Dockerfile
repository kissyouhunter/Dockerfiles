FROM python:3.10.8-alpine3.16

ADD ./ /app

RUN rm -f Dockerfile \
    && pip install openai \
    && pip install pyTelegramBotAPI

ENV TZ=Asia/Shanghai

WORKDIR /app

ENTRYPOINT python -u chat.py
