import time
import sys
import socket

#host = socket.scoket(socket.AF_INET,socket.SOCK_STREAM)
s = socket.socket()
host = socket.gethostname()
print("server will start on host: ",host)
port = 8081
s.bind((host,port))
print("")
print("Server will binding to host and port successfully")
print("")
s.listen(1)
conn,addr = s.accept()
print(s.accept)
print(conn)
print(addr,"Has connected to the server and is now online")
print("")
while(1):
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("mssg is sent successfully")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ",incoming_message)
    print("")
