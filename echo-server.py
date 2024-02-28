# echo-server.py

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO:
# 1: Bind the socket to the pynq board <CLIENT-IP> at port <LISTENING-PORT>
sock.bind(('0.0.0.0', 65432))
# 2: Accept connections
sock.listen()
print('Waiting for Connection')
conn, addr = sock.accept()
# 3: Receive bytes from the connection
with conn:
        print(f"Connected by {addr}")
        while True:
                data = conn.recv(1024)
# 4: Print the received message
                print(data.decode())
                if not data:
                        break

