import socket

c2 = socket.socket()

c2.connect(('localhost',9999))
print(c2.recv(1024).decode())
#print("message receved")


print(c2.recv(1024).decode())
#print("message receved")

