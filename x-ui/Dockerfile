FROM golang:bullseye AS builder
ARG XUI_REPO="https://github.com/vaxilu/x-ui"
RUN git clone ${XUI_REPO} --depth=1
WORKDIR /go/x-ui
RUN go build -a -ldflags "-linkmode external -extldflags '-static' -s -w"

FROM  alpine
LABEL org.opencontainers.image.authors="https://github.com/Chasing66"
COPY --from=builder /go/x-ui/x-ui /usr/local/bin/x-ui

ENV TZ=Asia/Shanghai
RUN apk add --no-cache ca-certificates tzdata 

ARG TARGETARCH
COPY --from=teddysun/xray /usr/bin/xray /usr/local/bin/bin/xray-linux-${TARGETARCH}
COPY --from=teddysun/xray /usr/share/xray/ /usr/local/bin/bin/

VOLUME [ "/etc/x-ui" ]
WORKDIR /usr/local/bin
CMD [ "x-ui" ]
