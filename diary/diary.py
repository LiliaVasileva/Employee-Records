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
        else:
            return 'No such record!'


    def search_record(self, date: str):
        if date in self.records.keys():
            result = "\n".join(self.records[date])
            return result
        else:
            return 'No records found!'

    def __file_save(self):
        path = f'records/{self.name}.json'
        file = open(f'records/{self.name}.json', "x")


# Test CODE, please run the code to check if the program works as expecred
# Creating an test diary to test instantiation of the class and creating file in records folder with name of the diary
test_diary = Diary('Test', 'monkey')
# Adding test record with on given data, to check if add_record method works proparly
test_diary.add_record('22.10.2022', 'This is test record')
# Adding  second test record with on given data, to check if it saves the record on existing date
test_diary.add_record('22.10.2022', 'This is second test record')
# Adding  second data with new record, to check if it saves the record on non existing date
test_diary.add_record('8.11.2022', 'This is third test record')
# Adding second test diary, to check if it saves a new file with the name
test_diary_second = Diary('Testov', 'chocolate')
# Adding a new record to the second test diary to check if program saves info in the correct file
test_diary_second.add_record('8.11.2022', 'This is test record')
# Check if the program returns the correct record when search_record methods is used, data as str is needed as an argument for the method
print(test_diary_second.search_record('8.11.2022'))
# If an non existing date is given should return "No records found"
print(test_diary_second.search_record('9.11.2022'))
# Test if delete record on existing data:
test_diary.delete_record('22.10.2022')
# Test if the record was delete
print(test_diary.search_record('22.10.2022'))
# Test when unvalid data is provided if it return "No such record"
print(test_diary.delete_record('22.10.2022'))

