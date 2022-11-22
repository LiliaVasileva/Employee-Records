import os
import hashlib
import hmac

"""
 Algorithm used from https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
"""

def hash_new_password(password):
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, password_hash


