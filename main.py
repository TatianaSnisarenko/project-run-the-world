from src.commands import (
    add_contact,
    change_contact,
    change_email,
    change_address,
    change_birthday,
    change_contact,
    parse_input,
    add_birthday,
    find_by_phone,
    find_by_email,
    find_by_address,
    show_contact,
    show_contact,
    show_all_contacts,
    parse_input,
    add_birthday,
    change_birthday,
    show_all_birthdays,
    add_note,
    show_all_notes,
    show_help,
    delete_contact,
    find_by_tags)
from src.errors.error_messages import generic_invalid_command_format_message
from src.models.address_book import AddressBook
from src.models.notes import Notes
from src.constants import available_commands
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession


def main():
    book = AddressBook()
    book = book.read_from_file()
    notes = Notes()
    notes = notes.read_from_file()
    print('Welcome to the assistant bot!')

    session = PromptSession(completer=WordCompleter(
        available_commands, ignore_case=True, sentence=True))
    while True:
        user_input = session.prompt('Enter a command: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            book.save_to_file()
            notes.save_to_file()
            print('Good bye!')
            break
        elif command == 'help':
            print(show_help())
        elif command == 'add-note':
            print(add_note(notes))
        elif command == 'add':
            print(add_contact(book))
        elif command == 'change':
            print(change_contact(args, book))
        elif command == 'change-email':
            print(change_email(args, book))
        elif command == 'change-address':
            print(change_address(args, book))
        elif command == 'change-birthday':
            print(change_birthday(args, book))
        elif command == 'change-phone':
            print(change_contact(args, book))
        elif command == 'phone':
            pass
            #print(show_phone(args, book))
        elif command == 'show-contact':
            print(show_contact(args, book))
        elif command == 'contacts':
            print(show_all_contacts(book))
        elif command == 'add-birthday':
            print(add_birthday(args, book))
        elif command == 'show-contact':
            print(show_contact(args, book))
        elif command == 'notes':
            print(show_all_notes(notes))
        elif command == 'birthdays':
            print(show_all_birthdays(book))
        elif command == 'find-by-phone':
            print(find_by_phone(args, book))
        elif command == 'find-by-email':
            print(find_by_email(args, book))
        elif command == 'find-by-address':
            print(find_by_address(args, book))
        elif command == 'delete-contact':
            print(delete_contact(args, book))
            print(show_all_contacts(book))
        elif command == 'change-birthday':
            print(change_birthday(args, book))
        elif command == 'notes':
            print(show_all_notes(notes))
        elif command == 'birthdays':
            print(show_all_birthdays(args, book))
        elif command == 'find-by-tag':
            print(find_by_tags(args, notes))
        else:
            print(generic_invalid_command_format_message)


if __name__ == '__main__':
    main()
