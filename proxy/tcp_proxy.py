import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
clientnext = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
hostnext = socket.gethostname()
port = 4444
portnext = 444

server.bind((host, port))
server.listen(5)

print("host =",host,"port =",port)
client, address = server.accept()

print("Connection to", hostnext, portnext)
clientnext.connect((hostnext,portnext))

while True:
    print("Connection recieved from", client, address)
    message = client.recv(1024).decode()
    print("Recieved from", host, port)
    print("message: ", message)
    clientnext.send(message.encode('ascii'))
    print("Sent to", hostnext, portnext)


    #client.send(message.encode('ascii'))
    #print("Sent to", host, port)
    #response = client.recv(1024).decode()
    #print(response)

#print("Connection to", host, portnext)
#client.connect((host,portnext))

#while True:
    #print("Connection recieved from", client, address)
    #message = client.recv(1024).decode()
    
    #client.send(message.encode('ascii'))
    #print("Sent to", host, port)
    #response = client.recv(1024).decode()
    #print(response)