import socket

c1=socket.socket()

c1.connect(('localhost',9999))
print(c1.recv(1024).decode())

chat= input("enter your message : ")
c1.send(bytes(chat,'utf-8'))
#print("message send")
