# import socket
# c=socket.socket()
# c.connect(("localhost",9999))
# x=c.recv(100).decode()
# print(x)

####decode
# import socket
# c=socket.socket()
# c.connect(("localhost",9999))
# name=input("enter your name:")
# c.send(name.encode())
# x=c.recv(100).decode()
# print(x)


####  unlimited sending of msg
import socket
c=socket.socket()
c.connect(("localhost",9999))
while True:
    x=c.recv(100).decode()
    print("Server:",x)
    client_msg=input("Client:")
    c.send(client_msg.encode())
