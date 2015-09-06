#! /usr/bin/python

import socket
import sys
import json

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the port where the server is listening
server_address = ('172.31.15.170', 10000)
#server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address

sock.connect(server_address)

try:
    while True:
        #send data
        message = {}
        message['A'] = raw_input("Input A:")
        message['B'] = raw_input("Input B:")
        message['C'] = raw_input("Input C:")
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(json.dumps(message))

        data = sock.recv(4096)
        print >>sys.stderr, 'received "%s"' % data

        d = json.loads(data)
        print 'recv dict:', d

finally:
    print >>sys.stderr, 'closing socket'
    sock.close
