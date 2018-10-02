import sys
import time
import socket

s = socket.socket()
host = input(str("enter the name of the server"))
port  = 8081
s.connect((host,port))
print("connected to server successfully")
while(1):
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ",incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("mssg is sent successfully")
    print("")
