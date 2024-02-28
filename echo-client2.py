# echo-client2.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO: 
# 1: Connect the socket (sock) to the <SERVER-IP> and choosen port <LISTENING-PORT>
sock.connect(('192.168.2.99',65432))
# 2: Send the message "Hello world!\n"
for i in range(5):
    msg = bytes(input("Message to send:\n")+ '\n','utf-8')
    sock.sendall(msg)
# 3: Close the socket
sock.close()
