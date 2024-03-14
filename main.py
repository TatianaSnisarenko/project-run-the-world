from src.commands import (
    add_contact,
    change_contact,
    show_phone,
    show_all_contacts,
    parse_input,
    add_birthday,
    find_by_phone,
    show_birthday,
    show_contact,
    show_all_birthdays,
    add_note,
    show_all_notes,
    show_help,
    delete_contact)
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
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(book))
        elif command == 'change':
            print(change_contact(args, book))
        elif command == 'phone':
            print(show_phone(args, book))
        elif command == 'contacts':
            print(show_all_contacts(book))
        elif command == 'add-birthday':
            print(add_birthday(args, book))
        elif command == 'show-birthday':
            print(show_birthday(args, book))
        elif command == 'show-contact':
            print(show_contact(args, book))
        elif command == 'notes':
            print(show_all_notes(notes))
        elif command == 'birthdays':
            print(show_all_birthdays(book))
        elif command == 'find-by-phone':
            print(find_by_phone(args, book))
        elif command == 'find-by-email':
            pass
            #print(find_by_email(args, email))
        elif command == 'find-by-address':
            pass
            #print(find_by_address(args, address))
        elif command == 'delete':
            print(delete_contact(args, book))
            print(show_all_contacts(book))
        else:
            print(generic_invalid_command_format_message)


if __name__ == '__main__':
    main()
