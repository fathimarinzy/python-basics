# import socket
# s=socket.socket()
# s.bind(("localhost",9999))
# s.listen()
# print("waiting for connection")
# while True:
#     c,address=s.accept()
#     print("connected",address)
#     c.send("hhhhhai".encode())

###decode
# import socket
# s=socket.socket()
# s.bind(("localhost",9999))
# s.listen()
# print("waiting for connection")
# while True:
#     cc,address=s.accept()
#     name=cc.recv(100).decode()
#     print("connected",address,name)
#     cc.send("thankyou for connecting".encode())


####  unlimited sending of msg
import socket
s=socket.socket()
s.bind(("localhost",9999))
s.listen()
print("waiting for connection")
while True:
    cc,address=s.accept()           
    print("connected",address)   
    while True:
        server_msg =input("Server:")
        cc.send(server_msg.encode())
        x=cc.recv(100).decode()
        print("rinzy:",x)