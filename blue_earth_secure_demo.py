# ===============================================================
# 🔵 BLUE AI TECHNOLOGIES™ — Secure Demo
# Blue Earth — Scrypt + Fernet key derivation (public version)
# ===============================================================

import os
import base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet

# Parameters (safe for public demo)
N = 2**14
r = 8
p = 1

def derive_key(password: bytes, salt: bytes) -> bytes:
    kdf = Scrypt(salt=salt, length=32, n=N, r=r, p=p)
    return base64.urlsafe_b64encode(kdf.derive(password))

def encrypt_message(message: str, password: str):
    salt = os.urandom(16)
    key = derive_key(password.encode(), salt)
    f = Fernet(key)
    token = f.encrypt(message.encode())
    return base64.urlsafe_b64encode(salt + token).decode()

def decrypt_message(encrypted: str, password: str):
    decoded = base64.urlsafe_b64decode(encrypted.encode())
    salt, token = decoded[:16], decoded[16:]
    key = derive_key(password.encode(), salt)
    f = Fernet(key)
    return f.decrypt(token).decode()

if __name__ == "__main__":
    msg = "Blue Earth secure demo running."
    pwd = "demo_password"
    enc = encrypt_message(msg, pwd)
    dec = decrypt_message(enc, pwd)
    print("Encrypted:", enc)
    print("Decrypted:", dec)
