from assistant.src.models.field import Field


class Content(Field):
    def __init__(self, content: str):
        super().__init__(content)

    def __eq__(self, other):
        if isinstance(other, Content):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
