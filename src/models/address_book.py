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

    def create_record(self, name: str, phone: str) -> None:
        record = Record(name, phone)
        self.add_record(record)

    def add_record(self, record: Record) -> None:
        if self.data.get(record.name) != None:
            raise KeyError
        self.data[record.name] = record

    def change_record_phone(self, name: str, phone: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.edit_phone(phone)

    def change_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.change_birthday(birthday)

    def change_record_address(self, name: str, address: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.add_birthday(birthday)
    
    def change_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.change_birthday(birthday)

    def change_record_email(self, name: str, email: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.change_email(email)

    def change_record_name(self, old_name: str, new_name: str) -> None:
        existing_record: Record = self.data[Name(old_name)]
        existing_record.change_name(new_name)

    def show_record(self, name: str) -> list:
        existing_record = self.data[Name(name)]
        return [existing_record.to_dict()]

    def delete_record(self, name: str) -> None:
        del self.data[Name(name)]

    def delete_phone(self, name: str, phone: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.delete_phone(phone)

    def get_record_birthdays_per_week(self, per_days: int) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays, per_days)

    def get_record_contacts(self) -> list:
        return [record.to_dict() for record in self.data.values()]
