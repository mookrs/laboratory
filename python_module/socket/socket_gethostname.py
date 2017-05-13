import socket


for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    try:
        print('%15s : %s' % (host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('%15s : ERROR: %s' % (host, msg))
