from cryptography.fernet import Fernet

class Encrypt():
    def __init__(self):
        self.encrypted = ""

    def save_key(self):
        self.key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key)
        return self.key
        print(self.key)

    def encrypt_password(self, message, key):
        self.key = key
        encoded_message = message.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        return(encrypted_message)


class Decrypt(Encrypt):
    super().__init__(self)
    
    def load_key():
        return open("secret.key", "rb").read()
    
    def decrypt_password(self, encrypted_message):
        self.key = load_key
        self.encrypted_message = encrypted_message
        f = Fernet(self.key)
        decrypted_message = f.decrypt(encrypted_message)

        print(decrypted_message.decode())


if __name__ == "__main__":
    enc_my_pass = input("Do you want to encrypt password (True/False) ? : ")
    if enc_my_pass.lower() == "true":
        user_password = input("Please enter your password: ")
        password = Encrypt()
        user_key = password.save_key()
        encrypted = password.encrypt_password(user_password, user_key)
        print("Encrypted password: {} ".format (encrypted))
        print ("Key: {}".format(user_key))
    

    else:
        user_encrypted = input ("Please enter your encrypted password: ")
        user_key = input("Please enter your key to decrypt: ")
        user_decrypt = Decrypt()
        decrypted = user_decrypt.decrypt_password(user_encrypted)

