from socket import *
import time
serverIP = "127.0.0.1"
serverPort = 7896
clientSocket = socket(AF_INET, SOCK_STREAM)
name = raw_input("Enter your name:")
note = raw_input("Enter your note:")
packet = str(name)+"*"+str(note)
clientSocket.connect((serverIP,serverPort)) 
clientSocket.send(packet)
name = raw_input("Enter your name:") 
clientSocket.send(name)
response = clientSocket.recv(1024)
print "From Server:", response
clientSocket.close()
