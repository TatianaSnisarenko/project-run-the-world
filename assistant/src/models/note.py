from assistant.src.models.tag import Tag
from assistant.src.models.title import Title
from assistant.src.models.content import Content
from assistant.src.errors.errors import ValidationError
from assistant.src.errors.error_messages import invalid_note_id_format_error_message
from assistant.src.errors.error_messages import tag_already_exists_error_message_template
from assistant.src.errors.error_messages import tag_doenst_exist_error_message_template


class Note:
    def __init__(self, title: str = '', content: str = '', tags: list = [], id: int = None) -> None:
        self.title = Title(title)
        self.content = Content(content)
        self.tags = [Tag(tag) for tag in tags if tag]
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Note):
            return (
                self.title == other.title
                and self.content == other.content
                and self.tags == other.tags
            )
        return False

    def change_title(self, title: str) -> None:
        self.title = Title(title.strip())

    def change_content(self, content: str) -> None:
        self.content = Content(content.strip())

    def add_tag(self, tag: str) -> None:
        new_tag = Tag(tag.strip())
        if new_tag in self.tags:
            raise ValidationError(
                tag_already_exists_error_message_template.format(tag=new_tag.value, id=self.id))
        self.tags.append(new_tag)

    def change_tag(self, old_tag: str, new_tag: str) -> None:
        existing_tag = Tag(old_tag.strip())
        if existing_tag not in self.tags:
            raise ValidationError(
                tag_doenst_exist_error_message_template.format(tag=existing_tag.value, id=self.id))
        for index, t in enumerate(self.tags):
            if existing_tag == t:
                self.tags[index] = Tag(new_tag.strip())

    def has_tag(self, tag: str):
        return Tag(tag.strip()) in self.tags

    def has_in_title(self, line: str) -> bool:
        return line.strip() in self.title.value

    def has_in_content(self, line: str) -> bool:
        return line.strip() in self.content.value

    def __hash__(self):
        return hash(self.title, self.content, tuple(self.tags))

    def __str__(self):
        str_tags = [str(tag.value) for tag in self.tags]
        return f"Note id: [{self.id}], title: [{self.title.value}], content: [{self.content.value}], tags: [{', '.join(str_tags)}]"
    
    def __repr__(self):
        str_tags = [str(tag.value) for tag in self.tags]
        return f"Note id [{self.id}] title [{self.title.value}] content [{self.content.value}] tags [{', '.join(str_tags)}]"

    def to_dict(self):
        return {
            "Id": self.id,
            "Tags": ", ".join([str(tag) for tag in self.tags]),
            "Title": str(self.title),
            "Content": str(self.content)
        }

    @staticmethod
    def validate_and_get_id(id: str) -> int:
        try:
            return int(id.strip())
        except:
            raise ValidationError(invalid_note_id_format_error_message)
