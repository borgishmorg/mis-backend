import os
import hashlib
from typing import Union


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


def check_password_hash(
    password: str, 
    hash: Union[str, bytes]
) -> bool:
    if type(hash) is str:
        hash = bytes.fromhex(hash)

    new_hash = generate_password_hash(password, hash[:32])

    return hash == new_hash
