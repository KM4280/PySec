import socket

proxyS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

hostProxy = socket.gethostname()
portProxy = 4444

proxyS.bind((hostProxy, portProxy))
proxyS.listen(5)

while True:
    # Attendre une connexion client
    print("host =",hostProxy,"port =",portProxy)
    clientS, addressClient = proxyS.accept()

    # Recevoir les données du client
    print("Connection recieved from", clientS, addressClient)
    message = clientS.recv(1024).decode()
    print("Recieved from", hostProxy, portProxy)
    print("message: ", message)

    # Créer un socket pour le serveur
    serverS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Extraire l'adresse IP et le port du serveur à partir de la demande du client
    addressServer = message.split(b'\r\n')[1].split(b' ')[1]
    addressServer = addressServer.split(b':')
    hostServer = addressServer[0]
    portServer = int(addressServer[1])

    # Se connecter au serveur
    print("Connection to", hostServer, portServer)
    serverS.connect((hostServer, portServer))

    # Envoyer les données au serveur
    print("Sent to", hostServer, portServer)
    serverS.sendall(message.encode('ascii'))

    # Recevoir les données du serveur
    print("Connection recieved from", serverS, addressServer)
    response = serverS.recv(1024).decode()
    print("Recieved from", hostServer, portServer)
    print("réponse: ", response)

    # Fermer la connexion avec le serveur
    serverS.close()
    print("Connection with Server closed")

    # Envoyer les données au client
    clientS.sendall(response.encode('ascii'))
    print("Sent to", clientS, addressClient)

    # Fermer la connexion avec le client
    clientS.close()
    print("Connection with Client closed")
