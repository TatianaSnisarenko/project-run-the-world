from src.commands import (
    add_contact,
    change_contact,
    show_contact,
    show_all_contacts,
    parse_input,
    add_birthday,
    change_birthday,
    show_all_birthdays,
    add_note,
    show_all_notes,
    show_help,
    change_tag,
    find_by_title,
    find_by_content,
    find_by_tags,
    sort_by_tag,
    show_note,
    delete_note)
from src.errors.error_messages import generic_invalid_command_format_message
from src.models.address_book import AddressBook
from src.models.notes import Notes
from src.constants import available_commands
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.styles import Style
from pygments.lexers.sql import SqlLexer

style = Style.from_dict({
    'completion-menu.completion': 'bg:#008888 #ffffff',
    'completion-menu.completion.current': 'bg:#00aaaa #000000',
    'scrollbar.background': 'bg:#88aaaa',
    'scrollbar.button': 'bg:#222222',
})


def main():
    book = AddressBook()
    book = book.read_from_file()
    notes = Notes()
    notes = notes.read_from_file()
    print('Welcome to the assistant bot!')

    session = PromptSession(completer=WordCompleter(
        available_commands, ignore_case=True, sentence=True), lexer=PygmentsLexer(SqlLexer), style=style)
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
            print(add_contact(args, book))
        elif command == 'change':
            print(change_contact(args, book))
        elif command == 'show-contact':
            print(show_contact(args, book))
        elif command == 'contacts':
            print(show_all_contacts(book))
        elif command == 'add-birthday':
            print(add_birthday(args, book))
        elif command == 'change-birthday':
            print(change_birthday(args, book))
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
