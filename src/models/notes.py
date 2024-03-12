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

    # def change_record_phone(self, name: str, phone: str) -> None:
    #     existing_record = self.data[Name(name)]
    #     existing_record.edit_phone(phone)

    # def add_record_birthday(self, name: str, birthday: str) -> None:
    #     existing_record = self.data[Name(name)]
    #     existing_record.add_birthday(birthday)

    def get_notes(self) -> list:
        return [str(note) for id, note in self.data.items()]

    def get_dict_notes(self) -> list:
        return [note.to_dict() for id, note in self.data.items()]

    # def show_record_birthday(self, name: str) -> str:
    #     existing_record = self.data[Name(name)]
    #     return str(existing_record.birthday) if existing_record.birthday else f'Birthday is not added for {name}'

    # def delete(self, name: str) -> None:
    #     self.data.pop(Name(name), None)

    # def get_record_birthdays_per_week(self) -> list:
    #     contact_birthdays = [{'name': str(name), 'birthday': record.birthday.birth_date}
    #                          for name, record in self.data.items() if record.birthday is not None]
    #     return get_birthdays_per_week(contact_birthdays)

    # def get_record_contacts(self) -> list:
    #     return [': '.join((str(name), str(record.phone))) for name, record in self.data.items()]
