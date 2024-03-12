from src.models.field import Field
from src.errors.errors import ValidationError


class Email(Field):
    def __init__(self, email: str):
        super().__init__(email)

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
    

    @staticmethod
    def validate_email(email: str) -> str:
        valid_email = email.strip()
        if "@" not in valid_email and "." not in valid_email:
            raise ValidationError("Sorry, you have entered an invalid email")
        return valid_email