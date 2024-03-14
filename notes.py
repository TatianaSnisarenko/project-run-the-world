from collections import UserDict
import pickle
import os
from src.models.note import Note
from errors.error_messages import empty_notes_error_message
from src.errors import EmptyNotesError


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

    def add_note(self, title: str, content: str, tags: list) -> None: #tags: list of strings
        pass


    def show_notes(self) -> list: #list of dictionaries(to_dict)
        pass
    

    def show_note(self, id:str) -> None:
        pass


    def delete_note(self, id:str) -> None:
        pass


    def change_title(self, id:str, title: str) -> None:
        pass
    

    def change_content(self, id:str, content: str) -> None:
        pass


    def add_tag(self, id:str, tag: str) -> None:
        pass


    def change_tag(self, id:str, old_tag:str, new_tag:str) -> None:
        pass
    

    def find_by_tag(self, tag:str) -> list: #list of dictionaries(to_dict)
        pass


    def find_by_title(self, title:str) -> list: #list of dictionaries(to_dict)            
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_title(title)]


    def find_by_content(self, content:str) ->  list: #list of dictionaries(to_dict)
        if len(self.data) == 0:
            raise EmptyNotesError(empty_notes_error_message)
        return [note.to_dict() for id, note in self.data.items()
                if note.has_in_content(content)]
    

    def sort_by_tags(self, tags: list) -> list: #list of dictionaries: новий вид списку - подумати як вивести; list of strings
        pass






