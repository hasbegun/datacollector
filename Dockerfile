FROM alpine:latest

RUN apk -U add \
        gcc \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
        musl-dev \
        libressl-dev \
        python3-dev \
        py-pillow \
        py-pip \
        curl ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/* \
    && pip install --upgrade pip \
    && pip install Scrapy pyyaml

WORKDIR /workspace/app

COPY entrypoint.sh /workspace/entrypoint.sh
RUN chmod +x /workspace/entrypoint.sh

ENTRYPOINT ["/workspace/entrypoint.sh"]
CMD ["scrapy"]
