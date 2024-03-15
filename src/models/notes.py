from collections import UserDict
import pickle
import os
from src.models.note import Note
from src.models.tag import Tag
from src.models.title import Title


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
    
    def change_existing_tag(self, id, old_tag, new_tag):
        tag_id = int(id.strip())
        for k, note in self.data.items():
            if k == tag_id:
                list_t = note.tags
                i = list_t.index(Tag(old_tag))
                list_t[i] = Tag(new_tag)
                return note

    def sort_tag(self, tag1, tag2):
        pass

    def show_exist_note(self, id):
        tag_id = int(id.strip())
        for k, note in self.data.items():
            if k == tag_id:
                return note

    def delete_exist_note(self, id):
        tag_id = int(id.strip())
        for k in self.data.keys():
            if k == tag_id:
                 self.data.pop(tag_id)
                 return self.data
                

    def get_notes(self) -> list:
        return [str(note) for id, note in self.data.items()]

    def get_dict_notes(self) -> list:
        return [note.to_dict() for id, note in self.data.items()]
    
    def __str__(self):
        return self.data
    
    def __rep__(self):
        return self.data

