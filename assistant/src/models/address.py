from assistant.src.models.field import Field


class Address(Field):
    def __init__(self, address: str):
        super().__init__(address.strip())

    def __eq__(self, other):
        if isinstance(other, Address):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
