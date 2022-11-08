from typing import Tuple
import os
import hashlib
import hmac
import json

def hash_new_password(password):
    """
    Hash the provided password with a randomly-generated salt and return the
    salt and hash to store in the database.
    """
    salt = os.urandom(16)
    password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt, password_hash

def is_correct_password(salt, password_hash, password):
    """
    Given a previously-stored salt and hash, and a password provided by a user
    trying to log in, check whether the password is correct.
    """
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    )

class SaveUser:
    def save_user(self):
        path = f'data/{self.username}.json'
        if not os.path.isfile(path):
            file = open(f'data/{self.username}.json', "x")
            data = {
                'username': self.username,
                'password': self.password,
                'salary': self.salary,
                'email': self.email,
            }
            with open(f'data/{self.username}.json', "w") as f:
                json.dump(data ,f, indent=4)
        else:
            pass


class EditUser:
    def edit_user(self,value):
        path = f'data/{self.username}.json'
        if not os.path.isfile(path):
            return
        with open(f'data/{self.username}.json', "r+") as f:
            data = json.load(f)
        if value == 'username':
            data[value] = self.username
            os.rename(f, self.username)
        elif value == 'password':
            data[value] = self.password
        elif value == 'salary':
            data[value] = self.salary
        elif value == 'email':
            data[value] = self.email
        with open(f'data/{self.username}.json', "r+") as f:
            json.dump(data ,f, indent=4)

class DeleteUser:
    def delete(self):
        os.remove(f'data/{self.username}.json')
        del self


class User(SaveUser, EditUser, DeleteUser):
    def __init__(self, username, password, salary, email):
        self.username = username
        self.password = password
        self.salary = salary
        self.email = email

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value
        self.edit_user('username')

    @property
    def password(self):
        salt, password_hash = self.__password
        return f'{salt}, {password_hash}'

    @password.setter
    def password(self, value):
        self.__password = hash_new_password(value)
        self.edit_user('password')


    @property
    def password(self):
        salt, password_hash = self.__password
        return f'{salt}, {password_hash}'

    @password.setter
    def password(self, value):
        self.__password = hash_new_password(value)
        self.edit_user('password')


    def __str__(self):
        return f"Username: {self.username},Password: {self.password}, Salary: {self.salary}$, Email: {self.email} "



my_user = User('Test', 'monkey', 300, 'lilia.vvasileva@gmail.com')

my_user.save_user()
my_user2 = User('Vasilev', 'chocolate', 300, 'kamen.vvasileva@gmail.com')
my_user2.save_user()
