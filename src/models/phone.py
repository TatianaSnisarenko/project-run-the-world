from src.models.field import Field
from src.errors.errors import ValidationError
from src.errors.error_messages import invalid_phone_number_error_message


class Phone(Field):
    def __init__(self, phone_number: str):
        super().__init__(self.clear_phone_number(phone_number))

    def __eq__(self, other):
        if isinstance(other, Phone):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def clear_phone_number(phone_number: str) -> str:
        cleared_phone_number = phone_number.strip()
        if not phone_number.isdigit() or len(cleared_phone_number) != 10:
            raise ValidationError(invalid_phone_number_error_message)
        return cleared_phone_number
