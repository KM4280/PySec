import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

server.bind((host, port))
server.listen(5)

print("host =",host,"port =",port)
client, address = server.accept()

while True:
