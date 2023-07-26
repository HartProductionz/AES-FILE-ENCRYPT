# AES File Encryption using (pycryptodome) Library
# (Make sure to install it
# on your machine prior to running)
# Created on 7/25/23

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_file(key, input_file, output_file=None):
    if not output_file:
        output_file = input_file + ".enc"

    chunk_size = 64 * 1024  # 64KB
    init_vector = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)

    with open(input_file, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(init_vector)

            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % AES.block_size != 0:
                    chunk += b' ' * (AES.block_size - len(chunk) % AES.block_size)

                encrypted_chunk = cipher.encrypt(chunk)
                outfile.write(encrypted_chunk)

def decrypt_file(key, input_file, output_file=None):
    if not output_file:
        output_file = os.path.splitext(input_file)[0]

    chunk_size = 64 * 1024  # 64KB

    with open(input_file, 'rb') as infile:
        init_vector = infile.read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv=init_vector)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break

                decrypted_chunk = cipher.decrypt(chunk)
                outfile.write(decrypted_chunk.rstrip())

if __name__ == "__main__":
    # Replace 'your_key_hex' with the hexadecimal representation of your desired encryption key
    encryption_key_hex = 'c8213a2e8efa2ecbfd9e27342b7a92402fce0ccc620d1e5abddb6d0f80f486dd'
    encryption_key = bytes.fromhex(encryption_key_hex)

    input_file_path = "C:/Users/domin/Downloads/Test.txt"  # Replace with the path to the file you want
                                                        # to encrypt/decrypt

    encrypt_file(encryption_key, input_file_path)
    print("File encrypted.")

    # Decryption example
   # decrypt_file(encryption_key, 'C:/Users/domin/Downloads/Test.txt')
    #print("File decrypted.")
