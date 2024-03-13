from src.models.field import Field
import re


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
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        valid_email = email.strip()
        if email_pattern.match(valid_email):
            print(f"{email} is a valid email address.")
        else:
            print(f"{email} is not a valid email address.")
        return valid_email
    

    

