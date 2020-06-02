#!/usr/bin/python3
import sys, os

#settings
webroot = "/www"
webredir = "https://www.yahoo.com/"
input = sys.stdin
header1 = str(input.readline())
header = header1
url = ""
host = ""
while header1 != "\r\n":
  if header1.lower().find('get') == 0:
    urltype = "get"
    url = header1.lower()[4:].split()[0]
  if header1.lower().find('post') == 0:
    urltype = "post"
    url = header1.lower()[5:].split()[0]
  if header1.lower().find('head') == 0:
    urltype = "head"
    url = header1.lower()[5:].split()[0]
  if header1.lower().find('host:') == 0:
    host = header1.lower()[5:].split()[0]
  if header1.lower().find('accept-encoding:') == 0:
    encoding = header1.lower()[16:].split()
  if header1.lower().find('user-agent:') == 0:
    agent = header1.lower()[12:-2]
  header1 = str(input.readline())
  header = header + header1
if url == "/":
	url = webroot + '/index.html'
else:
  url = webroot + url
#d = "<html><body>Welcome " + header + "<P><hr>\r\n" + str(url) + "</body></html>"
if os.path.exists(url):
  if url[-2:] == "py":
    d = os.popen('/usr/bin/python3 ' + url).read()
  elif url[-3:] == "php":
    d = os.popen('/usr/bin/php7 ' + url).read()
  elif url[-2:] == "js":
    d = os.popen('/usr/bin/node ' + url).read()
  else:
    file = open(url)
    d = file.read()
    file.close()
  leng = len(d) + 1
  print("HTTP/1.1 200 OK")
  print("Content-Type: text/html")
  print("Content-Length: " + str(leng))
  print("Connection: close")
  print("Accept-Ranges: bytes")
  print("")
  print(d)
  print("")
else:
  print("HTTP/1.1 302 Found")
  print("Location: " + webredir)
  print("")
