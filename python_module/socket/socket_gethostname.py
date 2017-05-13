import socket


for host in ['homer', 'www', 'www.python.org', 'nosuchname']:
    print(host)
    try:
        hostname, aliases, addresses = socket.gethostbyname_ex(host)
        print('Hostname:', hostname)
        print('Aliases :', aliases)
        print('Addresses:', addresses)
    except socket.error as msg:
        print('%15s : ERROR: %s' % (host, msg))
