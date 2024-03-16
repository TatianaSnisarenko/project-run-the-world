from assistant.src.models.name import Name
from assistant.src.models.phone import Phone
from assistant.src.models.birthday import Birthday
from assistant.src.models.email import Email
from assistant.src.models.address import Address

RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.


class Record:
    def __init__(self, name: str, phone: str = '', email: str = '', birthday: str = '', address: str = ''):
        self.name = Name(name)
        self.email = Email(email) if email.strip() else None
        self.birthday = Birthday(birthday) if birthday.strip() else None
        self.address = Address(address) if address.strip() else None
        self.phones = []
        self.phones.append(Phone(phone))

# phone

    def change_phone(self, old_phone: str, new_phone: str) -> None:
        old_phone_obj = Phone(old_phone.strip())
        new_phone_obj = Phone(new_phone.strip())
        phone_found = False
        for i, p in enumerate(self.phones):

            if p == old_phone_obj:
                self.phones[i] = new_phone_obj
                phone_found = True
                break
        if not phone_found:
            raise KeyError(f'''{RED}The wise speak only of what they know! 
                           Phone number not found in the record{RESET}''')

    def delete_phone(self, phone: str):
        existing_phone = Phone(phone.strip())
        if existing_phone in self.phones:
            self.phones.remove(existing_phone)
        else:
            raise ValueError(f'''{RED}The wise speak only of what they know!  
                             Phone number not found in the record{RESET}''')

    def add_birthday(self, birthday) -> None:
        self.birthday = Birthday(birthday)

# birthday

    def change_birthday(self, new_birthday) -> None:
        self.birthday = Birthday(new_birthday)

# email
    def change_email(self, new_email) -> None:
        self.email = Email(new_email)

# address

    def change_address(self, new_address) -> None:
        self.address = Address(new_address)

    def edit_phone(self, phone) -> None:
        self.phone = Phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phones == other.phones and self.birthday == other.birthday and self.email == other.email and self.address == other.address
        return False

    # self.address
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
