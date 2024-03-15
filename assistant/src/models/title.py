from assistant.src.models.field import Field


class Title(Field):
    def __init__(self, title: str):
        super().__init__(title)

    def __eq__(self, other):
        if isinstance(other, Title):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
