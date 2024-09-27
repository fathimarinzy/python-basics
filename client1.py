import socket
c=socket.socket()
c.connect(("localhost",9999))
x=c.recv(100).decode()
print(x)