# echo-client.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO:
# 1: Connect the socket (sock) to the <SERVER-IP> and choosen port <LISTENING-PORT>
sock.connect(('192.168.2.99', 65432)) # the port is the one that server is listening.
# 2: Send the message "Hello world!\n"
sock.send(b'Hello world!\n')
# 3: Close the socket
sock.close()
