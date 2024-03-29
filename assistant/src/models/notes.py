from collections import UserDict
import pickle
import os
from assistant.src.models.note import Note
from assistant.src.models.record import Record
from assistant.src.errors.errors import EmptyNotesError
from assistant.src.errors.error_messages import empty_notes_error_message, note_doesnt_exist_error_message
from collections import defaultdict


class Notes(UserDict):

    note_id = 1
    filename = 'notes.bin'

    def save_to_file(self):
        with open(Notes.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        if os.path.exists(self.filename):
            with open(Notes.filename, "rb") as file:
                notes = pickle.load(file)
                if notes.data.keys():
                    max_id = max(notes.data.keys())
                    Notes.note_id = max_id + 1
                return notes
        else:
            return Notes()

    def create_note(self, title: str, content: str, tags: list) -> None:
        note = Note(title, content, tags, Notes.note_id)
        if self.data.get(note.id) != None:
            raise KeyError
        if note in self.data.values():
            raise ValueError
        self.data[note.id] = note
        Notes.note_id += 1

    def show_note(self, id: str) -> list:
        note_id = Note.validate_and_get_id(id)
        existing_note = self.data[note_id]
        return [existing_note.to_dict()]

# list of dictionaries(to_dict)
    def find_record_by_title(self, title: str) -> list:
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_title(title)]

    # list of dictionaries(to_dict)
    def find_record_by_content(self, content: str) -> list:
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_content(content)]

    def find_record_by_tags(self, tags: list) -> dict:
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        if not tags:
            raise ValueError
        result = []
        for tag in tags:
            for note in self.data.values():
                if note.has_tag(tag):
                    result.append(self.convert_to_dict_by_tag(tag, note))
        return result

    def delete_note(self, id: str) -> None:
        note_id = Note.validate_and_get_id(id)
        del self.data[note_id]

    def find_by_title(self, title: str) -> list:  # list of dictionaries(to_dict)
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_title(title)]

    def find_by_content(self, content: str) -> list:  # list of dictionaries(to_dict)
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_content(content)]

    def get_notes(self) -> list:
        return [str(note) for id, note in self.data.items()]

    def get_dict_notes(self) -> list:
        return [note.to_dict() for id, note in self.data.items()]

    def __str__(self):
        return self.data

    def __rep__(self):
        return self.data

    def change_title(self, existing_note, new_title: str) -> None:
        existing_note.change_title(new_title)

    def validate_and_get_note(self, note_id: str) -> Note:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError(note_doesnt_exist_error_message)
        return existing_note

    def change_content(self, existing_note, new_content: str) -> None:
        existing_note.change_content(new_content)

    def add_tag(self, note_id: str, new_tag: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError(note_doesnt_exist_error_message)
        existing_note.add_tag(new_tag)

    def change_tag(self, note_id: str, old_tag: str, new_tag: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError(note_doesnt_exist_error_message)
        existing_note.change_tag(old_tag, new_tag)

    def convert_to_dict_by_tag(self, tag: str, note: Record):
        return {
            "Tag": tag.strip(),
            "Id": note.id,
            "Tags": ", ".join([str(tag) for tag in note.tags]),
            "Title": str(note.title),
            "Content": str(note.content)
        }

    def sort_records_by_tags(self) -> dict:
        tags = {tag.value for id, note in self.data.items()
                for tag in note.tags}
        return sorted(self.find_record_by_tags(tags), key=lambda x: x['Tag'])

    def change_tag(self, note_id: str, old_tag: str, new_tag: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError(note_doesnt_exist_error_message)
        existing_note.change_tag(old_tag, new_tag)

    def convert_to_dict_by_tag(self, tag: str, note: Record):
        return {
            "Tag": tag.strip(),
            "Id": note.id,
            "Tags": ", ".join([str(tag) for tag in note.tags]),
            "Title": str(note.title),
            "Content": str(note.content)
        }
