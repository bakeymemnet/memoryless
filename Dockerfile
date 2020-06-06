From alpine:latest

RUN apk update
RUN apk add busybox-extras python3 php7 nodejs wget openrc
COPY inetd.conf /etc/inetd.conf
COPY web2.py /usr/bin/web2.py
RUN chmod 755 /usr/bin/web2.py
RUN mkdir /www
RUN echo "<html><body><center>These aren&apos;t the droids you&apos;re looking for.</center></body></html>" > /www/index.html

EXPOSE 80

CMD ["/usr/sbin/inetd"]
