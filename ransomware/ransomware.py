from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import shutil
import socket
import os

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

with open("private_key.pem", "wb") as f:
    f.write(pem_private_key)

with open("public_key.pem", "wb") as f:
    f.write(pem_public_key)

folder = input("Entrez le dossier cible: ")

if os.path.exists("backup_folder"):
    shutil.rmtree("backup_folder")
shutil.copytree(folder, 'backup_folder')

client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = socket.gethostname()
port = 444
print("Connection to", host, port)
client.connect((host, port))

for root, dirs, files in os.walk("backup_folder"):
    for file in files:
        with open(os.path.join(root, file), "rb") as f:
            data = f.read()
            public_key = serialization.load_pem_public_key(
                pem_public_key,
                backend=default_backend()
            )
            encrypted_data = public_key.encrypt(
                data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            client.sendall(encrypted_data)

with open("buffer_file", "rb") as f:
    data = f.read()
    private_key = serialization.load_pem_private_key(
        pem_private_key,
        password=None,
        backend=default_backend()
    )
    decrypted_data = private_key.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    with open("decrypted_buffer_file", "wb") as f:
        f.write(decrypted_data)
