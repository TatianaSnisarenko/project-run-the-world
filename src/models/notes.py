from collections import UserDict
import pickle
import os
from src.models.note import Note
from src.errors.errors import EmptyNotesError
from src.errors.error_messages import empty_notes_error_message


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
