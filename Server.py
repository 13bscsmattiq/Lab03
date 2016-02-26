
from socket import*
import zipfile
serverPort = 7896
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(("127.0.0.1" ,serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
storage=[]
while 1:
    connectionSocket, addr = serverSocket.accept()
    filename = "received_note";
    with open(filename, 'wb') as f:
        packet = connectionSocket.recv(1024)
        f.write(packet)
        f.close()
        print('Successfully write the file')
        name = packet[1:packet.index("*")]
        note = packet[packet.index("*")+5:len(packet)]
        storage.append(name)
        storage.append(note)
        name = connectionSocket.recv(1024)
        if name in storage:
            index = storage.index(name)
            note = storage[index+1]
            connectionSocket.send(note)
        print storage
        
