# memoryless
Low memory web service

Just as we have gone from servers to instances, instances to containers, and containers to functions. The idea of memoryless to to move low usage services to non running services. With a few small servers you can provide many apps without the need for many resources. Using memoryless and containers with inteligent load balances services can be ramped up during the day and turned on to memoryless systems at night to save money. It also reduces an applications carbon footprint. Simplicity and demand based services.

Currently the system is designed around Alpine linux.

```Packages needed
apk add busybox-extras
edit /etc/inetd.conf
rc-service inetd start
rc-update add inetd
apk add python3
for php support
apk add php7
for node support
apk add nodejs

Copy the web2.py in /usr/bin
Copy inetd.conf to /etc```
