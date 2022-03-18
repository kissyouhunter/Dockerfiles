FROM python:3.7.12-alpine3.15

MAINTAINER kissyouhunter

COPY ./submit.py ./docker-entrypoint.sh /root/

RUN apk update \
    && apk add bash tzdata \
    && pip3 install telethon \
    && mkdir -p /telethon \
    && chmod a+x /root/docker-entrypoint.sh && mv /root/docker-entrypoint.sh /bin/docker-entrypoint \
    && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >  /etc/timezone
    
WORKDIR /telethon

ENTRYPOINT ["/bin/docker-entrypoint"]

CMD ["/bin/bash"]