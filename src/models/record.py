from src.models.name import Name
from src.models.phone import Phone
from src.models.birthday import Birthday
from src.models.email import Email
from src.models.address import Address


#Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
class Record:
    def __init__(self, name: str, email: str = '', birthday: str = None, address: str = ''):
        self.name = Name(name.strip())
        self.email = Email(email.strip())
        self.birthday = Birthday(birthday.strip())
        self.address = Address(address)
        self.phones = []

#name
        
    def change_name(self, old_name, new_name):    
        if str(self.name) == old_name:
            self.name = Name(new_name) 
    
#phone
    def add_phone(self, phones):
        for phone_number in phones:
            phone = Phone(phone_number)
            if phone is not None:
                self.phones.append(phone.strip())

    def change_phone(self, old_phone, new_phone):
        phone_found = False
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)
                phone_found = True
        if not phone_found:
                raise ValueError('Phone number not found in the record')
        
    def delete_phone (self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise ValueError('Phone number not found in the record')

#birthday
        
    def add_birthday(self, birthday) -> None:
        self.birthday = Birthday(birthday)

    def change_birthday(self, old_birthday, new_birthday):
        if str(self.birthday) == old_birthday:
            self.birthday = Birthday(new_birthday) 

#email
    def add_email(self, email) -> None:
        self.email = Email(email)

    def change_email(self, old_email, new_email):
        if str(self.email) == old_email:
            self.email = Email(new_email) 

#address
    def add_address(self, address) -> None:
        self.address = Address(address)

    def change_address(self, old_address, new_address):
        if str(self.address) == old_address:
            self.address = Address(new_address) 

#other
    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phones == other.phones and self.birthday == other.birthday and self.email == other.email and self.address == other.address
        return False

    def __hash__(self):
        return hash((self.name, tuple(self.phones), self.birthday, self.address, self.email))

    def __str__(self):
        birthday_str = f', birthday: {
            self.birthday.value}' if self.birthday else ''
        email_str = f', email: {
            self.email.value}' if self.email else ''
        address_str = f', address: {
            self.address.value}' if self.address else ''
        return f'Contact name: {self.name.value}, phones: {", ".join(str(phone) for phone in self.phones)}' + birthday_str + email_str + address_str
