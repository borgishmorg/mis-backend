import os
import hashlib


def generate_password_hash(
    password: str, 
    salt: bytes = None
):
    if salt is None:
        salt = os.urandom(32)

    password_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'), 
        salt, 
        100000 
    )
    storage = salt + password_hash
    return storage
