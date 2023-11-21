from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import shutil
import socket
import os

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(pem_private_key.splitlines()[0])

pem_public_key = private_key.public_key().public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem_public_key.splitlines()[0])

private_key_file = open("example-rsa.pem", "w")
private_key_file.write(pem_private_key.decode())
private_key_file.close()

public_key_file = open("example-rsa.pub", "w")
public_key_file.write(pem_public_key.decode())
public_key_file.close()

folder = input("entrez le dossier cible: ")
if os.path.exits("backup_folder"):
    shutil.rmtree("backup_folder")
shutil.copytree(folder, 'backup_folder')


client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

print("Connection to", host, port)
client.connect((host,port))

os.listdir()


dir = os.path.dirname(os.path.realpath(__file__))
priv = rsa

