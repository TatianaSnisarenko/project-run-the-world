from collections import UserDict
from src.user_birthdays import get_birthdays_per_week
import pickle
import os
from src.models.name import Name
from src.models.record import Record


class AddressBook(UserDict):

    filename = 'address_book.bin'

    def save_to_file(self):
        with open(AddressBook.filename, "wb") as file:
            pickle.dump(self, file)


    def read_from_file(self):
        if os.path.exists(self.filename):
            with open(AddressBook.filename, "rb") as file:
                return pickle.load(file)
        else:
            return AddressBook()
        

    def create_record(self, name: str, phones: list, email: str, address: str, birthday: str) -> None:
        pass


    def add_record_phone(self, name:str, phone:str) -> None:
        pass


    def change_record_phone(self, name: str, old_phone:str, new_phone:str) -> None:
        pass


    def show_records(self) -> list: #list of dictionaries(to_dict)
        pass


    def show_record(self, name:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_name(self, name:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_phone(self, phone:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_email(self, email:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_address(self, address:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_birthday(self, birthday:str) -> list: #list of dictionaries(to_dict)
        pass


    def delete_record(self, name:str) -> None:
        pass


    def change_record_name(self, old_name:str, new_name:str) -> None:
        pass


    def change_record_address(self, name:str, new_address:str) -> None:
        pass


    def change_record_birthday(self, name:str, new_birthday:str) -> None:
        pass


    def show_record_birthdays(self, days: int) -> list: #list of dictionaries(to_dict)
        pass





