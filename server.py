import socket
from threading import *
from time import sleep

s= socket.socket()
print('server created')

s.bind(('localhost',9999))

s.listen(2)
print("waiting for connection")

# after connect with client
def client1(condition):
     while condition:
                global c1
                c1,addr1 = s.accept()
                print("connected with ",addr1)

                c1.send(bytes('welcome to server','utf-8'))
                global chat
                chat = c1.recv(1024).decode()
              #  print("message receved")
                sleep(1)
                c1.close()



def client2(condition):
        while condition:
                global c2
                c2, addr2 = s.accept()
                print("connected with ", addr2)

                c2.send(bytes('welcome to server', 'utf-8'))

                c2.send(bytes(chat,'utf-8'))
             #   print("message  send to c2")
                sleep(1)
                c2.close()
condition=True
t1= Thread(target=client1,args=(condition,))
t2=Thread(target=client2,args=(condition,))

t1.start()
t2.start()

