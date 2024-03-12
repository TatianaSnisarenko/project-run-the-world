from src.models.tag import Tag
from src.models.title import Title
from src.models.content import Content


class Note:
    def __init__(self, title: str = '', content: str = '', tags: list = [], id: int = None) -> None:
        self.title = Title(title)
        self.content = Content(content)
        self.tags = [Tag(tag) for tag in tags]
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Note):
            return (
                self.title == other.title
                and self.content == other.content
                and self.tags == other.tags
            )
        return False

    def __hash__(self):
        return hash(self.title, self.content, tuple(self.tags))

    def __str__(self):
        str_tags = [str(tag.value) for tag in self.tags]
        return f'Note id: [{self.id}], title: [{self.title.value}], content: [{self.content.value}], tags: [{', '.join(str_tags)}]'

    def to_dict(self):
        return {
            "Id": self.id,
            "Tags": ", ".join([str(tag.value) for tag in self.tags]),
            "Title": self.title.value,
            "Content": self.content.value
        }
