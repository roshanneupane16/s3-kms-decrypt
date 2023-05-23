import base64
from Crypto.Cipher import AES
import sys

def unpad(data):
    pad_size = ord(data[-1:])
    return data[:-pad_size]

if len(sys.argv) != 4:
    print("Usage: python decrypt_file.py <Plaintext-KMS-DEK> <IV> <Encrypted-BAK-filename>")
    sys.exit(1)

block_size = AES.block_size
chunk_size = block_size * 1024
base64_key = sys.argv[1]
key = base64.b64decode(base64_key)
iv = base64.b64decode(sys.argv[2])

input_filename = sys.argv[3]
output_filename = f"{input_filename}.out"

cipher = AES.new(key, AES.MODE_CBC, iv)

with open(input_filename, 'rb') as input_file, open(output_filename, 'wb') as output_file:
    while True:
        encrypted_chunk = input_file.read(chunk_size)
        if len(encrypted_chunk) == 0:
            break
        decrypted_chunk = cipher.decrypt(encrypted_chunk)
        output_file.write(decrypted_chunk if len(input_file.peek(chunk_size)) else unpad(decrypted_chunk))

print(f"Finished decrypting {output_filename}")
