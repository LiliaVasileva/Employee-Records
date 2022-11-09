from typing import Tuple
import os
import hashlib
import hmac
import json
from password.password import  hash_new_password


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
        if value == 'password':
            data[value] = self.password
        elif value == 'salary':
            print(self.salary)
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

    @property
    def password(self):
        salt, password_hash = self.__password
        return f'{salt}, {password_hash}'

    @password.setter
    def password(self, value):
        self.__password = hash_new_password(value)
        self.edit_user('password')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value
        self.edit_user('salary')

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
        self.edit_user('email')

    def __str__(self):
        return f"Username: {self.username},Password: {self.password}, Salary: {self.salary}$, Email: {self.email} "


# TEST Code
# Creating test_user to test instantiation of the class
test_user = User('Test', 'monkey', 100, 'test.testov@gmail.com')
#Saving file with test_user username as a name of the file in folder called data
test_user.save_user()
# Creating second user to test instantiation of the class
test_user_second = User('Testov', 'chocolate', 200, 'testov.test.com')
#Saving file with test_user username as a name of the file in folder called data
test_user_second.save_user()
# Test when instance atribute is changed if the file is updating the information for the user
test_user_second.salary = 1000
# Test __str__ method returs the correct information for the instance of the class
print(test_user_second)
# Test deleting the instance of the class
test_user_second.delete()

