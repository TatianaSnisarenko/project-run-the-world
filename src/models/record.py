from src.models.name import Name
from src.models.phone import Phone
from src.models.birthday import Birthday
from src.models.email import Email
from src.models.address import Address

RED = "\33[91m"
GREEN = "\033[32m"

# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name: str, phone: str = '', email: str = '', birthday: str = '', address: str = ''):
        self.name = Name(name)
        self.email = Email(email) if email.strip() else None
        self.birthday = Birthday(birthday) if birthday.strip() else None
        self.address = Address(address) if address.strip() else None
        self.phones = []
        self.phones.append(Phone(phone))
# name

    def change_name(self, new_name: str) -> None:
        self.name = Name(new_name)
# phone

    def change_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone.strip())
        new_phone_obj = Phone(new_phone.strip())
        phone_found = False
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone_obj:
                self.phones[i] = Phone(new_phone_obj)
                phone_found = True
        if not phone_found:
            raise ValueError(f'{RED}Phone number not found in the record')

    def delete_phone(self, phone: str):
        existing_phone = Phone(phone.strip())
        if existing_phone in self.phones:
            self.phones.remove(existing_phone)
        else:
            raise ValueError(f'{RED}Phone number not found in the record')
        
    def add_birthday(self, birthday) -> None:
        self.birthday = Birthday(birthday)

    def change_birthday(self, birthday) -> None:
        self.birthday = Birthday(birthday)

    def change_email(self, email) -> None:
        self.email = Email(email)

    def change_address(self, address) -> None:
        self.address = Address(address)

    def edit_phone(self, phone) -> None:
        self.phone = Phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phones == other.phones and self.birthday == other.birthday and self.email == other.email and self.address == other.address
        return False

    def __hash__(self):
        return hash((self.name, tuple(self.phones), self.birthday, self.address, self.email))

    def __str__(self):
        birthday_str = f', birthday: {self.birthday.value}' if self.birthday else ''
        email_str = f', email: {self.email.value}' if self.email else ''
        address_str = f', address: {self.address.value}' if self.address else ''
        phones_str = f', phones: {", ".join(str(phone) for phone in self.phones)}' if self.phones else ''

        return f'Contact name: {self.name.value}, ' + birthday_str + email_str + address_str + phones_str
    
    def to_dict(self) -> dict:
        return {
            "Name": self.name.value,
            "Phones": ", ".join([str(phone) for phone in self.phones]),
            "Email": str(self.email),
            "Birthday": str(self.birthday),
            "Address": str(self.address)
        }
