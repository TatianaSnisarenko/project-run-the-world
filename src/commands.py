from src.errors.error_messages import (
    input_error,
    parse_input_error_messages,
    add_contact_error_messages,
    change_contact_error_messages,
    show_phone_error_messages,
    show_all_error_messages,
    add_birthday_error_messages,
    show_birthday_error_messages,
    show_all_birthdays_error_messages,
    add_note_error_messages,
    show_all_notes_error_messages
)
from src.models.address_book import AddressBook
from src.models.notes import Notes
from src.functions import format_as_table
from src.constants import commands_description


@input_error(parse_input_error_messages)
def parse_input(user_input):
    user_input.lstrip()
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error(add_note_error_messages)
def add_note(notes: Notes):
    note_title = input('Enter title: ')
    note_text = input('Enter note content: ')
    tags = input('Enter tags separated by comma: ')
    note_tags = [tag.strip() for tag in tags.split(',')]
    notes.create_note(note_title, note_text, note_tags)
    return 'Note added.'


@input_error(add_contact_error_messages)
def add_contact(args, book: AddressBook):
    name, phone = args
    book.create_record(name, phone)
    return 'Contact added.'


@input_error(change_contact_error_messages)
def change_contact(args, book: AddressBook):
    name, phone = args
    book.change_record_phone(name, phone)
    return 'Contact updated.'


@input_error(show_phone_error_messages)
def show_phone(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError
    return book.show_record_phone(args[0])


@input_error(show_all_error_messages)
def show_all_contacts(book: AddressBook):
    contacts = book.get_record_contacts()
    if not contacts:
        raise ValueError
    return '\n'.join(contacts)


@input_error(show_all_notes_error_messages)
def show_all_notes(notes: Notes):
    note_list = notes.get_notes()
    if not notes:
        raise ValueError
    return format_as_table(notes.get_dict_notes(), 40)


@input_error(add_birthday_error_messages)
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.add_record_birthday(name, birthday)
    return 'Birthday added.'


@input_error(show_birthday_error_messages)
def show_birthday(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError
    return book.show_record_birthday(args[0])


@input_error(show_all_birthdays_error_messages)
def show_all_birthdays(book: AddressBook):
    if not book:
        raise ValueError
    birthdays = book.get_record_birthdays_per_week()
    return '\n'.join(birthdays) if birthdays else 'No birthdays for this week.'


@input_error([])
def show_help():
    return format_as_table(commands_description, 40)
