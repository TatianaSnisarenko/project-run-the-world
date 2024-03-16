from assistant.src.commands import (
    add_contact,
    change_record_phone,
    change_email,
    change_address,
    change_birthday,
    change_record_phone,
    parse_input,
    add_birthday,
    find_by_phone,
    find_by_email,
    find_by_address,
    find_by_brithday,
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
    find_by_tags,
    change_tag,
    find_by_title,
    find_by_content,
    find_by_tags,
    sort_by_tag,
    show_note,
    delete_note,
    change_content,
    change_title,
    add_tag)
from assistant.src.errors.error_messages import generic_invalid_command_format_message
from assistant.src.models.address_book import AddressBook
from assistant.src.models.notes import Notes
from assistant.src.constants import available_commands
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.sql import SqlLexer
from assistant.src.theme.enter_decorator import enter_decorator_func
from assistant.src.theme.exit_decorator import exit_decorator_func


style = Style.from_dict({
    'completion-menu.completion': 'bg:#006f9a #ffffff',
    'completion-menu.completion.current': 'bg:#008bc1 #000000',
    'scrollbar.background': 'bg:#4ba6c9',
    'scrollbar.button': 'bg:#222222',
})

@enter_decorator_func
def main():
    book = AddressBook()
    book = book.read_from_file()
    notes = Notes()
    notes = notes.read_from_file()

    session = PromptSession(completer=WordCompleter(
        available_commands, ignore_case=True, sentence=True), lexer=PygmentsLexer(SqlLexer), style=style)
    while True:
        user_input = session.prompt('The Precious is yours, do command, my friend: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit']:
            book.save_to_file()
            notes.save_to_file()
            exit_decorator_func()
            break
        elif command == 'help':
            print(show_help())
        elif command == 'add-note':
            print(add_note(notes))
        elif command == 'add-contact':
            print(add_contact(book))
        elif command == 'change-title':
            print(change_title(args, notes))
        elif command == 'change-content':
            print(change_content(args, notes))
        elif command == 'add-tag':
            print(add_tag(args, notes))
        elif command == 'change':
            print(change_record_phone(args, book))
        elif command == 'change-email':
            print(change_email(args, book))
        elif command == 'change-address':
            print(change_address(args, book))
        elif command == 'change-birthday':
            print(change_birthday(args, book))
        elif command == 'change-phone':
            print(change_record_phone(args, book))
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
        elif command == 'find-by-phone':
            print(find_by_phone(args, book))
        elif command == 'find-by-email':
            print(find_by_email(args, book))
        elif command == 'find-by-address':
            print(find_by_address(args, book))
        elif command == 'find-by-birthday':
            print(find_by_brithday(args, book))
        elif command == 'delete-contact':
            print(delete_contact(args, book))
        elif command == 'notes':
            print(show_all_notes(notes))
        elif command == 'birthdays':
            print(show_all_birthdays(args, book))
        elif command == 'change-tag':
            print(change_tag(args, notes))
        elif command == 'find-by-title':
            print(find_by_title(args, notes))
        elif command == 'find-by-tag':
            print(find_by_tags(args, notes))
        elif command == 'find-by-content':
            print(find_by_content(args, notes))
        elif command == 'sort-by-tag':
            print(sort_by_tag(args, notes))
        elif command == 'show-note':
            print(show_note(args, notes))
        elif command == 'delete-note':
            print(delete_note(args, notes))
        else:
            print(generic_invalid_command_format_message)


if __name__ == '__main__':
    main()
