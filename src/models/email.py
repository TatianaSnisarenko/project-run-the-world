from src.models.field import Field
from src.errors.errors import ValidationError
from src.errors.error_messages import invalid_email_error_message_template
import re


class Email(Field):
    def __init__(self, email: str):
        super().__init__(self.validate_and_get_email(email))

    def __eq__(self, other):
        if isinstance(other, Email):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
    

    @staticmethod    
    def validate_and_get_email(email: str) -> str:        
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        valid_email = email.strip()
        if email_pattern.match(valid_email):
            return valid_email
        else:
            raise ValidationError(invalid_email_error_message_template.format(email=email))

    

    

