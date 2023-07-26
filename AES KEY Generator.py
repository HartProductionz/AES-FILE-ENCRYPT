from Crypto.Random import get_random_bytes

def generate_aes_key(key_length=32):
    return get_random_bytes(key_length)

# Example usage:
aes_key = generate_aes_key(key_length=32)  # Generating a 32-byte (256-bit) AES key
print(aes_key.hex())  # Print the hexadecimal representation of the key
