from src.models.name import Name
from src.models.phone import Phone
from src.models.birthday import Birthday


class Record:
    def __init__(self, name: str, phone: str) -> None:
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None

    def add_birthday(self, birthday) -> None:
        self.birthday = Birthday(birthday)

    def change_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)

    def edit_phone(self, phone) -> None:
        self.phone = Phone(phone)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.name == other.name and self.phone == other.phone and self.birthday == other.birthday
        return False

    def __hash__(self):
        return hash(self.name, self.phone, self.birthday)

    def __str__(self):
        birthday_str = f', birthday: {self.birthday.value}' if self.birthday else ''
        return f'Contact name: {self.name.value}, phone: {self.phone.value}' + birthday_str
