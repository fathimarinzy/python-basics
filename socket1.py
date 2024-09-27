import socket
s=socket.socket()
s.bind(("localhost",9999))
s.listen()
print("waiting for connection")
while True:
    c,address=s.accept()
    print("connected",address)
    c.send("hhhhhai".encode())