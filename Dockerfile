From alpine:latest

RUN apk update
RUN apk add busybox-extras python3 php7 nodejs wget
RUN wget https://gitlab.com/bakeysf/memoryless/-/raw/master/inetd.conf -O /etc/inetd.conf
RUN wget https://gitlab.com/bakeysf/memoryless/-/raw/master/web2.py -O /usr/bin/web2.py
RUN chmod 755 /usr/bin/web2.py
RUN mkdir /www
RUN echo "These aren\'t the droids you\'re looking for." > /www/index.html

EXPOSE 80

CMD ["inetd"]
