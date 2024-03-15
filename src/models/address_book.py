from collections import UserDict
from src.user_birthdays import get_birthdays_per_week
import pickle
import os
from src.models.name import Name
from src.models.email import Email
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

    def create_record(self, name: str, phone: str, email: str, birthday: str, address: str ) -> None:
        record = Record(name, phone, email ,birthday, address)
        self.add_record(record)

    def add_record(self, record: Record) -> None:
        if not record.name:
            raise ValueError("Name cannot be empty.")
        self.data[record.name] = record

    def change_record_phone(self, name: str, new_phone: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_phone(new_phone)

    def change_record_birthday(self, name: str, new_birthday: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_birthday(new_birthday)

    def change_record_address(self, name: str, new_address: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_address(new_address)

    def change_record_email(self, name: str, new_email: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_email(new_email)

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
        existing_records = [record for record in self.data.values() if record.address == address]
        if existing_records:
            return '\n'.join([f"{record.name}: Phone - {record.phone}, Birthday - {record.birthday}, Address - {record.address}" for record in existing_records])
        else:
            return f'No contacts found with address {address}'


    def find_record_by_email(self, email: str) -> str: 
        existing_records = [record for record in self.data.values() if record.email == email]
        if existing_records:
            return '\n'.join([f"{record.name}: Phone - {record.phone}, Birthday - {record.birthday}, Email - {record.email}, Address - {record.address}" for record in existing_records])
        else:
            return f'No contacts found with email {email}'

    def show_record_contact(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        if existing_record:
            phones = ", ".join(str(phone) for phone in existing_record.phones) if existing_record.phones else "None"
            return f"{name}: Phone - {phones}, Birthday - {existing_record.birthday}, Email - {existing_record.email} ,Address - {existing_record.address}"
        else:
            return f'Contact with name {name} not found'

    def delete(self, name: str) -> None:
        self.data.pop(Name(name), None)
        
    def get_record_birthdays_per_week(self) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays)

    def get_record_contacts(self) -> list:
        contacts = [
            f"{name}: Phone - {', '.join(str(phone) for phone in record.phones)}, Birthday - {record.birthday}, Email - {record.email}, Address - {record.address}"
            if hasattr(record, 'phones') and record.phones else
            f"{name}: Phone - None, Birthday - {record.birthday}"
            for name, record in self.data.items()
        ]
        return contacts

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

    #def get_record_contacts(self) -> list:
     #   return [record.to_dict() for record in self.data.values()]
