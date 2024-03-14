from src.errors.error_messages import (
    parse_input_error_messages,
    add_contact_error_messages,
    change_contact_error_messages,
    show_phone_error_messages,
    show_all_error_messages,
    add_birthday_error_messages,
    show_birthday_error_messages,
    show_all_birthdays_error_messages,
    add_note_error_messages,
    show_all_notes_error_messages,
    change_birthday_error_messages
)
from src.errors.error_decorator import input_error
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
def add_contact(book: AddressBook):
    #name, phone, address = args
    name_add = input('Enter name: ')
    phone_add = input('Enter phone: ')
    #address_add = input('Enter address:')
    #email_add = input('Enter email:')
    book.create_record(name_add, phone_add)
    return 'Contact added.'


@input_error(change_contact_error_messages)
def change_contact(args, book: AddressBook):
    name, phone = args
    book.change_record_phone(name, phone)
    return 'Contact updated.'

#@input_error(show_contact_error_messages)
def show_contact(args, book: AddressBook):
    name = args[0] 
    return book.show_record_contact(name)

#@input_error(find_by_phone_error_messages)
def find_by_phone(args, book: AddressBook): 
    phone = args[0]
    contacts = book.get_record_contacts()

    # Extrahiere Telefonnummern und vergleiche sie
    phone_numbers = [contact.split("Phone - ")[1].split(",")[0].strip() for contact in contacts]
    if phone in phone_numbers:
        for contact in contacts:
            if f"Phone - {phone}" in contact:
                return f'Contact {phone} found successfully. {contact}'
    
    # Wenn die Telefonnummer nicht gefunden wurde
    return f'Contact {phone} not found.'



#@input_error(find_by_email_error_messages)
def find_by_email(args, book: AddressBook): 
    pass
#    email = args[0]  
#    return book.find_record_by_email(email)

#@input_error(find_by_address_error_messages)
def find_by_address(args, book: AddressBook): 
    pass
#    address = args[0]  
#    return book.find_record_by_address(address)

@input_error(show_phone_error_messages)
def show_phone(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError
    return book.show_record_phone(args[0])


#@input_error(show_all_error_messages)
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


@input_error(change_birthday_error_messages)
def change_birthday(args, book: AddressBook):
    if (len(args) != 2):
        raise ValueError
    name, birthday = args
    book.change_record_birthday(name, birthday)
    return 'Birthday changed.'


@input_error(show_birthday_error_messages)
def show_birthday(args, book: AddressBook):
    if (len(args) != 1):
        raise ValueError
    return book.show_record_birthday(args[0])


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
        raise KeyError()
    birthdays = book.get_record_birthdays_per_week(per_days)
    return format_as_table(birthdays, 40) if birthdays else 'No birthdays for next {days} days.'


@input_error([])
def show_help():
    return format_as_table(commands_description, 20)

#@input_error(delete_contact_error_messages)
def delete_contact(args, book: AddressBook):
    name = args[0]
    contacts = book.get_record_contacts()

    if name in [contact.split(":")[0].strip() for contact in contacts]:
        book.delete(name)
        return f'Contact {name} deleted successfully.'
    else:
        return f'Contact {name} not found.'
