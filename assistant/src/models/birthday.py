from datetime import datetime
import re
from assistant.src.models.field import Field
from assistant.src.errors.errors import ValidationError
from assistant.src.errors.error_messages import invalid_birthday_format_error_message


class Birthday(Field):
    def __init__(self, birthday: str):
        super().__init__(self.validate_and_get_value(birthday))

    def __eq__(self, other):
        if isinstance(other, Birthday):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    @property
    def birth_date(self):
        return datetime.strptime(self.value, '%d.%m.%Y') if self.value else None

    @staticmethod
    def validate_and_get_value(birthday: str) -> str:
        cleared_birthday = birthday.strip()
        pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
        if not bool(pattern.match(cleared_birthday)):
            raise ValidationError(invalid_birthday_format_error_message)
        try:
            date_object = datetime.strptime(cleared_birthday, '%d.%m.%Y')
            return cleared_birthday
        except ValueError:
            raise ValidationError(invalid_birthday_format_error_message)
