FROM debian:11.2-slim

MAINTAINER kissyouhunter

COPY ./docker-entrypoint.sh /root/

RUN apt update \
    && apt install -y wget systemctl \
    && apt install -y --no-install-recommends -y ca-certificates \
    && wget https://raw.githubusercontent.com/vaxilu/x-ui/master/install.sh && bash install.sh \
    && chmod a+x /root/docker-entrypoint.sh && mv /root/docker-entrypoint.sh /bin/docker-entrypoint
    
WORKDIR /root

ENTRYPOINT ["/bin/docker-entrypoint"]

CMD ["/bin/bash"]