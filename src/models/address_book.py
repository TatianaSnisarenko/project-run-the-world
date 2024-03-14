from collections import UserDict
from src.user_birthdays import get_birthdays_per_week
import pickle
import os
from src.models.name import Name
from src.models.phone import Phone
from src.models.record import Record
from src.models.address import Address


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
        #address: str
        # record = Record(name, phone, address)
        record = Record(name, phone)
        self.add_record(record)

    def add_record(self, record: Record) -> None:
        if self.data.get(record.name) != None:
            raise KeyError
        self.data[record.name] = record

    def change_record_phone(self, name: str, phone: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.edit_phone(phone)

    def change_record_address(self, name: str, address: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.edit_address(address)

    def add_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.add_birthday(birthday)

    def find_record_by_phone(self, phone: str) -> str:
        existing_record = None
        for record in self.data.values():
            if record.phone == phone:
                existing_record = record
                break

        if existing_record:
            return f"{existing_record.name}: Phone - {existing_record.phone}, Birthday - {existing_record.birthday}"
        else:
            return f'Contact with phone {phone} not found'

    def find_record_by_address(self, address: str) -> str: 
        pass

    def find_record_by_email(self, email: str) -> str: 
        pass

    def show_record_contact(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return f"{name}: Phone - {existing_record.phone}, Birthday - {existing_record.birthday}" if existing_record.name else f'Contact with name {name} not found'

    def show_record_phone(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return str(existing_record.phone)

    def show_record_birthday(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return str(existing_record.birthday) if existing_record.birthday else f'Birthday is not added for {name}'

    def delete(self, name: str) -> str:
        self.data.pop(Name(name), None)
        
    def get_record_birthdays_per_week(self) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays)

    def get_record_contacts(self) -> list:
        contacts = [
            f"{name}: Phone - {', '.join(str(phone) for phone in record.phones)}, Birthday - {record.birthday}"
            if hasattr(record, 'phones') and record.phones else
            f"{name}: Phone - None, Birthday - {record.birthday}"
            for name, record in self.data.items()
        ]
        return contacts

