import os
import hashlib
import hmac


def hash_new_password(password):
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, password_hash

def is_correct_password(salt, password_hash, password):
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

