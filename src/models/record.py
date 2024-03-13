from src.models.name import Name
from src.models.phone import Phone
from src.models.birthday import Birthday
from src.models.address import Address

class Record:
    def __init__(self, name: str, phone: str ) -> None:
        self.name = Name(name)
        self.phone = Phone(phone)
        #address: str
        #self.address = Address(address) 
        self.birthday = None
        #email: str
        #self.email = None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def edit_phone(self, phone) -> None:
        self.phone = Phone(phone)

    #def edit_address(self, address) -> None:
       # self.address = Address(address)

    # self.address == other.address and 
    def __eq__(self, other):
        if isinstance(other, Record):
            return (self.name == other.name and
                    self.phone == other.phone and
                    self.birthday == other.birthday)
        return False

    #self.address
    def __hash__(self):
        return hash(self.name, self.phone, self.birthday)

    def __str__(self):
        birthday_str = f', birthday: {self.birthday.value}' if self.birthday else ''
        # address_str = birthday_str = f', address: {self.address.value}' if self.address else ''
        # {address_str}
        # email_str = birthday_str = f', email: {self.email.value}' if self.email else ''
        # {email_str}
        return f'Contact name: {self.name.value}, phone: {self.phone.value}{birthday_str}'


