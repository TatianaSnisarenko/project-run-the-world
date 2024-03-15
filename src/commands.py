from src.errors.error_messages import (
    parse_input_error_messages,
    add_contact_error_messages,
    change_contact_error_messages,
    show_contact_error_messages,
    show_all_error_messages,
    add_birthday_error_messages,
    show_all_birthdays_error_messages,
    invalid_per_days_error_message,
    add_note_error_messages,
    show_all_notes_error_messages,
    find_by_tags_error_messages,
    change_birthday_error_messages,
    change_tag_error_messages,
    delete_note_error_messages,
    show_note_error_messages
)
from src.errors.error_decorator import input_error
from src.models.address_book import AddressBook
from src.models.notes import Notes
from src.errors.errors import ValidationError
from src.functions import format_as_table
from src.constants import commands_description

RED = "\33[91m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
RESET = "\033[0m"


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
    return f'{GREEN}Note added.{RESET}'


@input_error(add_contact_error_messages)
def add_contact(args, book: AddressBook):
    name, phone = args
    book.create_record(name, phone)
    return f'{GREEN}Contact added.{RESET}'


@input_error(change_contact_error_messages)
def change_contact(args, book: AddressBook):
    name, phone = args
    book.change_record_phone(name, phone)
    return f'{GREEN}Contact updated.{RESET}'


@input_error(show_contact_error_messages)
def show_contact(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError
    return format_as_table(book.show_record(args[0]), 40)


@input_error(show_all_error_messages)
def show_all_contacts(book: AddressBook):
    contacts = book.get_record_contacts()
    if not contacts:
        raise ValueError
    return format_as_table(contacts, 20)


@input_error(show_all_notes_error_messages)
def show_all_notes(notes: Notes):
    note_list = notes.get_notes()
    if not notes:
        raise ValueError
    return format_as_table(notes.get_dict_notes(), 40)


@input_error(change_tag_error_messages)
def change_tag(args, notes: Notes):
    id, old_tag, new_tag = args
    changed_note = notes.change_tag(id, old_tag, new_tag)
    return f'{GREEN}Tag changeed.{RESET}'


@input_error(add_note_error_messages)
def find_by_title(args, notes: Notes):
    title = args[0]
    result = notes.find_record_title(title)
    if result:
        return format_as_table(result, 40)
    else:
        return f"{YELLOW}There are no notes for such title: [{title}]{RESET}"


@input_error(add_note_error_messages)
def find_by_content(args, notes: Notes):
    text = args[0]
    result = notes.find_record_content(text)
    if result:
        return format_as_table(result, 40)
    else:
        return f"{YELLOW}There are no notes for such content: [{text}]{RESET}"


@input_error(find_by_tags_error_messages)
def find_by_tags(args, notes: Notes):
    tags = [tag.strip() for arg in args for tag in arg.split(',')]
    result = notes.find_record_tags(tags)
    if result:
        return format_as_table(result, 40)
    else:
        return f"{YELLOW}There are no notes for such tags: [{', '.join(tags)}]{RESET}"


@input_error(add_note_error_messages)
def sort_by_tag(args, notes: Notes):
    tag1, tag2 = args
    result = notes.sort_record_tag(tag1, tag2)
    return format_as_table(result, 40)


@input_error(show_note_error_messages)
def show_note(args, notes: Notes):
    if (len(args) != 1):
        raise ValueError
    return format_as_table(notes.show_note(args[0]), 40)


@input_error(delete_note_error_messages)
def delete_note(args, notes: Notes):
    if (len(args) != 1):
        raise ValueError
    notes.delete_note(args[0])
    return f'{GREEN}The note was deleted.{RESET}'


@input_error(add_birthday_error_messages)
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.add_record_birthday(name, birthday)
    return f'{GREEN}Birthday added.{RESET}'


@input_error(change_birthday_error_messages)
def change_birthday(args, book: AddressBook):
    if (len(args) != 2):
        raise ValueError
    name, birthday = args
    book.change_record_birthday(name, birthday)
    return f'{GREEN}Birthday changed.{RESET}'


@input_error(change_birthday_error_messages)
def change_birthday(args, book: AddressBook):
    if (len(args) != 2):
        raise ValueError
    name, birthday = args
    book.change_record_birthday(name, birthday)
    return f'{GREEN}Birthday changed.{RESET}'


@input_error(show_all_birthdays_error_messages)
def show_all_birthdays(args, book: AddressBook):
    days = args[0].strip()
    if len(args) != 1:
        raise ValueError()
    if not days.isdigit():
        raise ValidationError(invalid_per_days_error_message)
    per_days = int(days)
    if per_days < 1 or per_days > 365:
        raise ValidationError(invalid_per_days_error_message)
    if not book:
        raise KeyError
    birthdays = book.get_record_birthdays_per_week(per_days)
    return format_as_table(birthdays, 40) if birthdays else 'No birthdays for next {days} days.'


@input_error([])
def show_help():
    return format_as_table(commands_description, 20)
