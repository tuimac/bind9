FROM alpine:latest

EXPOSE 53/tcp
EXPOSE 53/udp

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash bind bind-dnssec-tools && \
    mkdir /etc/bind/named && \
    mkdir /var/log/bind

COPY entrypoint.sh /opt/entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
