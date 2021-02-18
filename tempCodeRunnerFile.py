from cryptography.fernet import Fernet
from kdf import derive_key

passphrase = b"hunter2"
key = derive_key(passphrase, salt_gen=True)
f = Fernet(key)

with open('plain.txt', 'rb') as file:
    plaintext = file.read()  # binary read

plaintext += b"Hey new data!"

with open('encrypted.txt', 'wb') as file:
    file.write(f.encrypt(plaintext))  # binary write