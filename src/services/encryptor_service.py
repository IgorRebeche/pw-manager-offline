from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
import hashlib
import os
from Cryptodome.Random import get_random_bytes

class EncryptorService:
    def __init__(self) -> None:
        pass

    def generate_salt(self):
        # generate a random salt
        return b64encode(get_random_bytes(AES.block_size)).decode('utf-8')

    def encrypt(self, salt, password, plain_text):
        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password.encode(), salt=b64decode(salt), n=2**14, r=8, p=1, dklen=32)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(
            bytes(plain_text, 'utf-8'))

        return '.'.join([
                b64encode(cipher_text).decode('utf-8'),
                b64encode(cipher_config.nonce).decode('utf-8'),
                b64encode(tag).decode('utf-8')
            ])
    
    def decrypt(self, salt, password, encrypted_data):
        # decode the dictionary entries from base64
        data = encrypted_data.split('.')
        salt = b64decode(salt)
        nonce = b64decode(data[1])
        
        cipher_text = b64decode(data[0])

        tag = b64decode(data[2])

        # generate the private key from the password and salt

        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return bytes.decode(decrypted)

    def create_256_bit_hash(self, text):
        m = hashlib.sha256(text.encode('UTF-8'))
        return m.hexdigest()