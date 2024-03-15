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
    
    def add_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.change_birthday(birthday)

    def change_record_birthday(self, name: str, new_birthday: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_birthday(new_birthday)

    def change_record_address(self, name: str, new_address: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_address(new_address)
    
    def change_record_birthday(self, name: str, birthday: str) -> None:
        existing_record = self.data[Name(name)]
        existing_record.change_birthday(birthday)

    def change_record_email(self, name: str, new_email: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.change_email(new_email)

    def find_record_by_phone(self, phone: str) -> list:
        matching_records = []
        for record in self.data.values():
            for phone_number in record.phones:
                if str(phone_number) == phone:
                    matching_records.append(record.to_dict())
                    break
        return matching_records

    def find_record_by_address(self, address: str) -> list:
        matching_records = []
        for record in self.data.values(): 
            if str(record.address).strip() == address.strip():
                matching_records.append(record.to_dict())
        return matching_records

    def find_record_by_email(self, email: str) -> list: 
        matching_records = []
        for record in self.data.values(): 
            if str(record.email).strip() == email.strip():
                matching_records.append(record.to_dict())
        return matching_records

    def find_record_by_birthday(self, birthday: str) -> list: 
        matching_records = []
        for record in self.data.values(): 
            if str(record.birthday).strip() == birthday.strip():
                matching_records.append(record.to_dict())
        return matching_records

    def delete(self, name: str) -> None:
        self.data.pop(Name(name), None)
        
    def get_record_birthdays_per_week(self) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays)

    def change_record_name(self, old_name: str, new_name: str) -> None:
        existing_record: Record = self.data[Name(old_name)]
        existing_record.change_name(new_name)

    def show_record(self, name: str) -> dict:
        existing_record = self.data[Name(name)]
        return [existing_record.to_dict()]

    def delete_record(self, name: str) -> None:
        del self.data[Name(name)]

    def delete_phone(self, name: str, phone: str) -> None:
        existing_record: Record = self.data[Name(name)]
        existing_record.delete_phone(phone)
    
    def show_record_birthday(self, name: str) -> str:
        existing_record = self.data[Name(name)]
        return str(existing_record.birthday) if existing_record.birthday else f'Birthday is not added for {name}'

    def get_record_birthdays_per_week(self, per_days: int) -> list:
        contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
                             for name, record in self.data.items() if record.birthday is not None]
        return get_birthdays_per_week(contact_birthdays, per_days)

    def get_record_contacts(self) -> list:
      return [record.to_dict() for record in self.data.values()]
