from cryptography.fernet import Fernet
key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(b"Hello World")


print(encrypted_message)

decrypted_message = encryption_type.decrypt(encrypted_message)
print(decrypted_message)