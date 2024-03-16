from assistant.src.errors.error_messages import (
    parse_input_error_messages,
    add_contact_error_messages,
    change_phone_error_messages,
    show_contact_error_messages,
    show_all_error_messages,
    add_birthday_error_messages,
    show_all_birthdays_error_messages,
    add_note_error_messages,
    show_all_notes_error_messages,
    change_birthday_error_messages,
    change_email_error_messages,
    change_address_error_messages,
    change_birthday_error_messages,
    find_by_tags_error_messages,
    invalid_per_days_error_message,
    find_by_phone_error_messages,
    find_by_email_error_messages,
    find_by_address_error_messages,
    delete_contact_error_messages,
    find_by_birthday_error_messages,
    change_tag_error_messages,
    delete_note_error_messages,
    show_note_error_messages,
    change_note_title_error_messages,
    change_note_content_error_messages,
    add_tag_error_messages
)
from assistant.src.errors.error_decorator import input_error
from assistant.src.models.address_book import AddressBook
from assistant.src.models.address import Address
from assistant.src.models.notes import Notes
from assistant.src.models.phone import Phone
from assistant.src.models.email import Email
from assistant.src.models.birthday import Birthday
from assistant.src.models.note import Note
from assistant.src.errors.errors import ValidationError
from assistant.src.functions import format_as_table
from assistant.src.constants import commands_description
from assistant.src.errors.errors import ValidationError
from assistant.src.errors.error_messages import invalid_phone_number_error_message

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
    note_title = input("The jorney starts here. Enter title: ")
    note_text = input('Write something wise, my dear friend. Enter note content: ')
    tags = input('And one more. Enter tags separated by comma: ')
    note_tags = [tag.strip() for tag in tags.split(',')]
    notes.create_note(note_title, note_text, note_tags)
    return f'{GREEN}Note added.{RESET}'


def validate_name(name: str) -> str:
    if len(name.strip()) < 1:
        raise ValueError(f"{RED}Do not tempt me! Name must be at least 1 character long.{RESET}")
    return name


def validate_phone(phone: str) -> str:
    try:
        return Phone.validate_and_get(phone)
    except ValidationError as ve:
        raise ValueError(str(ve))


def validate_birthday(birthday: str) -> str:
    try:
        validated_birthday = Birthday.validate_and_get_value(birthday)
        return validated_birthday
    except ValidationError as ve:
        raise ValueError(str(ve))


def validate_email(email: str) -> str:
    try:
        validated_birthday = Email.validate_and_get_email(email)
        return validated_birthday
    except ValidationError as ve:
        raise ValueError(str(ve))


@input_error(add_tag_error_messages)
def add_tag(args, notes: Notes):
    if (len(args) != 2):
        raise ValueError
    note_id, tag = args
    notes.add_tag(note_id, tag)
    return (f'''{GREEN}The world is changed. I feel it in the water. 
    I feel it in the earth. I smell it in the air.
    Tag added.{RESET}''')


@input_error(change_note_title_error_messages)
def change_title(args, notes: Notes):
    if (len(args) != 1):
        raise ValueError
    note_id = args[0]
    existing_note = notes.validate_and_get_note(note_id)
    new_title = input("Let's do it! Enter new title: ")
    notes.change_title(existing_note, new_title)
    return (f'''{GREEN}The world is changed. I feel it in the water. 
    I feel it in the earth. I smell it in the air.
    Note title changed.{RESET}''')


@input_error(change_note_content_error_messages)
def change_content(args, notes: Notes):
    if (len(args) != 1):
        raise ValueError
    note_id = args[0]
    existing_note = notes.validate_and_get_note(note_id)
    new_content = input('Hary up, my dear! Enter new content: ')
    notes.change_content(existing_note, new_content)
    return (f'''{GREEN}The world is changed. I feel it in the water. 
    I feel it in the earth. I smell it in the air.
    Note content changed.{RESET}''')


@input_error(add_tag_error_messages)
def add_tag(args, notes: Notes):
    if (len(args) != 2):
        raise ValueError
    note_id, tag = args
    notes.add_tag(note_id, tag)
    return (f'''{GREEN}The world is changed. I feel it in the water. 
    I feel it in the earth. I smell it in the air.
    Tag added.{RESET}''')


@input_error(add_contact_error_messages)
def add_contact(book: AddressBook):
    validated_name = ''
    validated_email = ''
    validated_birthday = ''
    validated_address = ''

    while True:
        name_add = input('Now enter name, my friend: ')
        if not name_add.strip():
            print(f"{YELLOW}Be carefull, my friend, Name can't be empty.{RESET}")
            continue
        try:
            validated_name = validate_name(name_add)
            break
        except ValueError as ve:
            print(ve)

    while True:
        phone_add = input('Enter phone, my friend: ')
        if not phone_add.strip():
            print(f"{YELLOW}Be carefull, my friend, Phone can't be empty.{RESET}")
            continue
        else:
            try:
                validated_phone = validate_phone(phone_add)
                break
            except ValueError as ve:
                print(ve)

    while True:
        email_add = input('Enter email, my friend: ')
        if not email_add.strip():
            break
        try:
            validated_email = validate_email(email_add)
            break
        except ValueError as ve:
            print(ve)

    while True:
        birthday_add = input('Enter birthday, my friend: ')
        if not birthday_add.strip():
            break
        try:
            validated_birthday = validate_birthday(birthday_add)
            break
        except ValueError as ve:
            print(ve)

    while True:
        address_add = input('Enter address, my friend: ')
        if not address_add.strip():
            break
        try:
            validated_address = address_add
            break
        except ValueError as ve:
            print(ve)

    book.create_record(validated_name, validated_phone,
                       validated_email, validated_birthday, validated_address)
    return (f'''{GREEN}
The world is changed. I feel it in the water. 
I feel it in the earth. I smell it in the air.
Contact added.
            {RESET}''')


@input_error(change_phone_error_messages)
def change_record_phone(args, book: AddressBook):
    if (len(args) != 3):
        raise ValueError
    name, old_phone, new_phone = args
    book.change_record_phone(name, old_phone, new_phone)
    return (f'''{GREEN}
The world is changed. I feel it in the water. 
I feel it in the earth. I smell it in the air.
Contact updated.
            {RESET}''')


@input_error(find_by_birthday_error_messages)
def find_by_brithday(args, book: AddressBook):
    birthday = args[0]
    matching_records = book.find_record_by_birthday(birthday)
    if not matching_records:
        return (f'''{YELLOW}
The wise speak only of what they know! 
No contact found with this birthday.
                {RESET}''')
    else:
        return format_as_table(matching_records, cell_width=20)


@input_error(find_by_phone_error_messages)
def find_by_phone(args, book: AddressBook):
    phone = args[0]
    matching_records = book.find_record_by_phone(phone)
    if not matching_records:
        return (f'''{YELLOW}
The wise speak only of what they know! 
No contact found with this phone number.
                {RESET}''')
    else:
        return format_as_table(matching_records, cell_width=20)


@input_error(find_by_email_error_messages)
def find_by_email(args, book: AddressBook):
    email = args[0]
    matching_records = book.find_record_by_email(email)
    if not matching_records:
        return (f'''{YELLOW}
The wise speak only of what they know! 
Do not tempt me! No contact found with this email.
                {RESET}''')
    else:
        return format_as_table(matching_records, cell_width=20)


@input_error(find_by_address_error_messages)
def find_by_address(args, book: AddressBook):
    address = args[0]
    matching_records = book.find_record_by_address(address)
    if not matching_records:
        return (f'''{YELLOW}
The wise speak only of what they know! 
No contact found with this address.
                {RESET}''')
    else:
        return format_as_table(matching_records, cell_width=20)


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
    return (f'''{GREEN}
The world is changed. I feel it in the water. 
I feel it in the earth. I smell it in the air.
Tag changed.
            {RESET}''')


@input_error(add_note_error_messages)
def find_by_title(args, notes: Notes):
    title = args[0]
    result = notes.find_record_title(title)
    if result:
        return format_as_table(result, 40)
    else:
        return (f'''{YELLOW}
What a pitty, my dear friend! 
There are no notes for such title: [{title}].
                {RESET}''')


@input_error(add_note_error_messages)
def find_by_content(args, notes: Notes):
    text = args[0]
    result = notes.find_record_content(text)
    if result:
        return format_as_table(result, 40)
    else:
        return (f'''
{YELLOW}What a pitty, my dear friend! 
 There are no notes for such content: [{text}].
                {RESET}''')


@input_error(find_by_tags_error_messages)
def find_by_tags(args, notes: Notes):
    tags = [tag.strip() for arg in args for tag in arg.split(',')]
    result = notes.find_record_tags(tags)
    if result:
        return format_as_table(result, 40)
    else:
        return (f'''{YELLOW}
What a pitty, my dear friend! 
There are no notes for such tags: [{', '.join(tags)}].
                {RESET}''')


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
    return (f'''{GREEN}
Death is just another path - one that we all must take.
The note was deleted.
            {RESET}''')


@input_error(add_birthday_error_messages)
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.add_record_birthday(name, birthday)
    return (f'''{GREEN}
The world is changed. I feel it in the water. 
I feel it in the earth. I smell it in the air.
Birthday added.
            {RESET}''')


@input_error(change_birthday_error_messages)
def change_birthday(args, book: AddressBook):
    if (len(args) != 2):
        raise ValueError
    name, birthday = args
    book.change_record_birthday(name, birthday)
    return (f'''{GREEN}
The world is changed. I feel it in the water. 
I feel it in the earth. I smell it in the air.
Birthday changed.
            {RESET}''')


@input_error(change_email_error_messages)
def change_email(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError(f'''{RED}
You shall not pass! 
Invalid number of arguments
                         {RESET}''')
    name, new_email = args
    book.change_record_email(name, new_email)
    return (f'''{GREEN}
My dear friend, now I can tell:
Email for contact {name} changed to {new_email}.
            {RESET}''')


@input_error(change_address_error_messages)
def change_address(args, book: AddressBook):
    if len(args) != 2:
        raise ValueError(f'''{RED}
You shall not pass! 
Invalid number of arguments.
                         {RESET}''')
    name, new_address = args
    book.change_record_address(name, new_address)
    return (f'''{GREEN}
My dear friend, now I can tell:
Address for contact {name} changed to {new_address}.
            {RESET}''')


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
    return format_as_table(birthdays, 40) if birthdays else (f'''{YELLOW}
What a pity, my dear friend! 
No birthdays for next {days} days.
    {RESET}''')


@input_error(find_by_tags_error_messages)
def find_by_tags(args, notes: Notes):
    tags = [tag.strip() for arg in args for tag in arg.split(',')]
    result = notes.find_by_tags(tags)
    if result:
        return format_as_table(result, 40)
    else:
        return (f'''{YELLOW}
What a pity, my dear friend!
There are no notes for such tags: [{', '.join(tags)}].
{RESET}''')


@input_error([])
def show_help():
    return format_as_table(commands_description, 20)


@input_error(delete_contact_error_messages)
def delete_contact(args, book: AddressBook):
    name = args[0]
    deleted = book.delete(name)
    if deleted:
        return (f'''{GREEN}
Death is just another path - one that we all must take.
Contact '{name}' deleted successfully.
{RESET}''')
    else:
        return (f'''{YELLOW}
What a pitty, my dear friend! 
Contact '{name}' not found.
{RESET}''')
