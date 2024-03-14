from collections import UserDict
import pickle
import os
from src.models.note import Note


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

    def get_notes(self) -> list:
        return [str(note) for id, note in self.data.items()]

    def get_dict_notes(self) -> list:
        return [note.to_dict() for id, note in self.data.items()]

    def change_title(self, note_id: str, new_title: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError("Note with provided ID does not exist")
        existing_note.change_title(new_title)

    def change_content(self, note_id: str, new_content: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError("Note with provided ID does not exist")
        existing_note.change_content(new_content)

    def add_tag(self, note_id: str, new_tag: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError("Note with provided ID does not exist")
        existing_note.add_tag(new_tag)

    def change_tag(self, note_id: str, old_tag: str, new_tag: str) -> None:
        int_id = Note.validate_and_get_id(note_id)
        existing_note = self.data.get(int_id)
        if existing_note is None:
            raise KeyError("Note with provided ID does not exist")
        existing_note.change_tag(old_tag, new_tag)