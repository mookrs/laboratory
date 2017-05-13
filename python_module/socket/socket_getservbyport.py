import socket
import urllib.parse

for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
    print(urllib.parse.urlunparse((socket.getservbyport(port), 'example.com', '/', '', '', '')))
