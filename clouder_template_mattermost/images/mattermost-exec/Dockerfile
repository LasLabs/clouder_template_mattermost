FROM clouder/base:3.4
MAINTAINER Ted Salmon <tsalmon@laslabs.com>

ENV MM_VERSION 3.6.2
ENV MM_BASE https://releases.mattermost.com/

ENV PACKAGES "ca-certificates curl wget"

RUN apk add --update $PACKAGES

WORKDIR /tmp

# Install glibc
RUN apk --no-cache add ca-certificates openssl \
    && wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub \
    && apk --no-cache -X http://apkproxy.heroku.com/sgerrand/alpine-pkg-glibc add glibc glibc-bin

# Install Elasticsearch
WORKDIR /opt

RUN mkdir -p /opt \
    && adduser -h /opt/elasticsearch -g elasticsearch -s /bin/bash -D elasticsearch

RUN ln -s elasticsearch elasticsearch-$ES_VERSION
USER elasticsearch
RUN set -x \
    && wget -O - "${ES_BASE}/elasticsearch-${ES_VERSION}.tar.gz" | tar -xz

ENV PATH /opt/elasticsearch/bin:$PATH

WORKDIR /opt/elasticsearch
RUN set -ex \
    && for path in \
        ./data \
        ./logs \
        ./config \
        ./config/scripts \
    ; do \
        mkdir -p "$path"; \
        chown -R elasticsearch:elasticsearch "$path"; \
    done

# Entrypoint
COPY docker-entrypoint.sh /

ENTRYPOINT ["/mattermost-entrypoint.sh"]
CMD ["mattermost"]
