from src.models.field import Field
from src.errors.errors import ValidationError
from src.errors.error_messages import invalid_name_format_error_message


class Name(Field):
    def __init__(self, name: str):
        super().__init__(self.validate_and_get_value(name))

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    @staticmethod
    def validate_and_get_value(name: str) -> str:
        cleared_name = name.strip()

        if not cleared_name:
            raise ValidationError(invalid_name_format_error_message)
        return cleared_name
