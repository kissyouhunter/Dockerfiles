FROM --platform=$TARGETPLATFORM metacubex/mihomo:v1.18.3

EXPOSE 8080

RUN apk update && apk add nginx

COPY ./dashboard/ /dashboard
COPY ./nginx.conf /etc/nginx
COPY ./start.sh /

ENTRYPOINT [ "sh", "/start.sh" ] 