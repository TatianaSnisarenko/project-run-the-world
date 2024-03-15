from assistant.src.models.field import Field


class Tag(Field):
    def __init__(self, tag: str):
        super().__init__(tag)

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)
