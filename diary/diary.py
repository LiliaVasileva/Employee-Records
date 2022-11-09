import os
import hashlib
import hmac
import json
from password.password import hash_new_password


class Diary:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.records = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value:
            self.__name = value
            self.__file_save()

    @property
    def password(self):
        salt, password_hash = self.__password
        return f'{salt}, {password_hash}'

    @password.setter
    def password(self, value: str):
        self.__password = hash_new_password(value)

    def add_record(self, date: str,text: str):
        if date in self.records.keys():
            self.records[date].append(text)
        else:
            self.records[date] = []
            self.records[date].append(text)

        with open(f'records/{self.name}.json', "w") as f:
            json.dump(self.records, f, indent=4)

    def delete_record(self, date: str):
        if date in self.records.keys():
            del self.records[date]

    def check_record(self, date: str):
        if date in self.records.keys():
            result = "\n".join(self.records[date])
            return result
        else:
            return 'No records found'

    def __file_save(self):
        path = f'records/{self.name}.json'
        file = open(f'records/{self.name}.json', "x")



my_diary = Diary('Test', 'monkey')
my_diary.add_record('22.10.2022', 'This is test record')
my_diary.add_record('22.10.2022', 'This is second test record')
my_diary.add_record('8.11.2022', 'This is third test record')
test2 = Diary('John', 'chocolate')
test2.add_record('8.11.2022', 'This is test record')