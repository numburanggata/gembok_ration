#!/usr/bin/env python3
# gem_decryptor.py
from cryptography.fernet import Fernet
import os

key = b'MTIzNDU2NzgxMjM0NTY3ODEyMzQ1Njc4MTIzNDU2Nzg='
cipher = Fernet(key)
dir = "/var/www/html/csirt/public"

for file in os.listdir(dir):
    if file.endswith(".gembok"):
        enc_path = os.path.join(dir, file)
        orig_path = enc_path[:-7]  # remove .gembok
        try:
            with open(enc_path, "rb") as f:
                enc = f.read()
            data = cipher.decrypt(enc)
            with open(orig_path, "wb") as f:
                f.write(data)
            os.remove(enc_path)
            print(f"Decrypted {file}")
        except:
            print(f"Failed {file}")
