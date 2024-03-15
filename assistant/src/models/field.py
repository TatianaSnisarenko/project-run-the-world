class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
