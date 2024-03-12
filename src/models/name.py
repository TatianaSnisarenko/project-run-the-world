from src.models.field import Field


class Name(Field):
    def __init__(self, name: str):
        super().__init__(name)

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
