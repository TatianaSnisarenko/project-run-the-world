from src.models.field import Field
from src.errors.errors import ValidationError
from src.errors.error_messages import invalid_name_error_message


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
        
    #returns true if validation was successful, otherwise false if after strip() name was empty
    @staticmethod
    def validate(name: str) -> str:
        cleared_name = name.strip()
        if not cleared_name:
            raise ValidationError(invalid_name_error_message)
        return cleared_name