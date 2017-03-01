FROM clouder/base:3.4
MAINTAINER Ted Salmon <tsalmon@laslabs.com>

ENV MM_VERSION 3.6.2
ENV MM_BASE https://releases.mattermost.com/

ENV PACKAGES "ca-certificates curl wget"

RUN apk add --update $PACKAGES

WORKDIR /tmp

RUN curl https://releases.mattermost.com/$MM_VERSION/mattermost-team-$MM_VERSION-linux-amd64.tar.gz | tar -xvz

EXPOSE 80

VOLUME /opt/mattermost/data

# Entrypoint
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["mattermost"]
