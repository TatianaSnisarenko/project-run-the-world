from src.errors.errors import ValidationError

RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"

generic_error_message = f'{RED}Something went wrong, please try again.{RESET}'
invalid_phone_number_error_message = f'{
    RED}Invalid phone number: must be 10 digits value.{RESET}'
invalid_birthday_format_error_message = f'{
    RED}Invalid birthday format: must be <DD.MM.YYYY>.{RESET}'
invalid_name_format_error_message = f'{
    RED}Invalid name format: name must not be empty.{RESET}'
invalid_note_id_format_error_message = f'{
    RED}Invalid note id: id must not be a valid number.{RESET}'
tag_already_exists_error_message_template = 'Such tag: [{tag}] is already present for the note with id: [{id}]'
tag_doenst_exist_error_message_template = 'Such tag: [{tag}] is not found for the note with id: [{id}]'
empty_notes_error_message = 'Notes are empty, please add new notes first'
invalid_email_error_message_template = 'Not a valid email provided: [{email}]. Please try again'
invalid_per_days_error_message = 'Invalid value: must be only numbers from 1 to 365'
empty_notes_error_message = 'Notes are empty. Please, use "add-note" command to add new notes.'

empty_notes_error_message = f'{
    RED}Notes are empty, please add new notes first{RESET}'
invalid_email_error_message_template = 'Not a valid email provided: [{email}]. Please try again'
invalid_per_days_error_message = f'{
    RED}Invalid value: must be only numbers from 1 to 365{RESET}'
empty_notes_error_message = f'{
    RED}Notes are empty. Please, use "add-note" command to add new notes.{RESET}'

generic_invalid_command_format_message = f'''{RED}Invalid "command" format.
Please use <help> to display
all available commands{RESET}'''

add_note_error_messages = {
    'FormatError': f'{RED}Such note is already present, please, use "change_note" command instead.{RESET}',
    'KeyError': f'{RED}Such note is already present, please, use "change_note" command instead.{RESET}'
}

show_note_error_messages = {
    'FormatError': f'{RED}Invalid "show-note" format. Command "show-note" must have 2 arguments: <show-note ID>.{RESET}',
    'KeyError': f'{RED}Such note with provided ID does not exist.{RESET}'
}

add_birthday_error_messages = {
    'FormatError': f'{RED}Invalid "add-birthday" format. Command "add-birthday" must have 3 arguments: <add-birthday Name DD.MM.YYYY>.{RESET}',
    'KeyError': f'{RED}Such name is not found, please, use "add" command to add new contact first.{RESET}',
    'ValidationError': invalid_birthday_format_error_message
}

add_contact_error_messages = {
    'FormatError': f'{RED}Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.{RESET}',
    'KeyError': f'{RED}Such name is already present, please, use "change" command instead.{RESET}',
    'ValidationError': invalid_phone_number_error_message
}
change_address_error_messages = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_address>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.'
}

change_contact_error_messages = {
    'FormatError': f'{RED}Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.{RESET}',
    'KeyError': f'{RED}Such name is not found, please, use "add" command instead.{RESET}',
    'ValidationError': invalid_phone_number_error_message
}

change_birthday_error_messages = {
    'FormatError': f'{RED}Invalid "change-birthday" format. Command "change-birthday" must have 3 arguments: <change-birthday Namenew_birthday>.{RESET}',
    'KeyError': f'{RED}Such name is not found, please, use "add" command instead.{RESET}',
    'ValidationError': invalid_birthday_format_error_message
}

change_email_error_messages = {
    'FormatError': 'Invalid "change-email" format. Command "change-email" must have 3 arguments: <change-email  Name  new_email>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.',
    'ValidationError': invalid_email_error_message_template
}


show_phone_error_messages = {
    'FormatError': 'Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.',
}

show_contact_error_messages = {
    'FormatError': f'{RED}Invalid "show-contact" format. Command "show-contact" must have 2 arguments: <show-contact Name>.{RESET}',
    'KeyError': f'{RED}Such name is not found, please, try again.{RESET}'
}

show_phone_error_messages = {
    'FormatError': f'{RED}Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.{RESET}',
    'KeyError': f'{RED}Such name is not found, please, try again.{RESET}'
}


find_by_tags_error_messages = {
    'FormatError': f'{RED}Invalid "find-by-tag" format. Command "find-by-tag" must have not less then 2 arguments: <find-by-tag tag1,tag2,tag3>.{RESET}',
}

find_by_phone_error_messages = {
    'FormatError': 'Invalid "find-by-phone" format. Command "find-by-phone" must have 2 arguments: <find-by-phone Phone>.',
    'KeyError': 'Such name is not found, please, try again.',
    'ValidationError': invalid_phone_number_error_message,
}

find_by_birthday_error_messages =  {
    'FormatError': 'Invalid "find-by-phone" format. Command "find-by-phone" must have 2 arguments: <find-by-phone Phone>.',
    'KeyError': 'Such name is not found, please, try again.',
    'ValidationError': invalid_birthday_format_error_message,
}

find_by_email_error_messages = {
    'FormatError': 'Invalid "find-by-email" format. Command "find-by-email" must have 2 arguments: <find-by-phone Email>.',
    'KeyError': 'Such name is not found, please, try again.'
}

find_by_address_error_messages = {
    'FormatError': 'Invalid "find-by-address" format. Command "find-by-address" must have 2 arguments: <find-by-address Email>.',
    'KeyError': 'Such name is not found, please, try again.'
}

find_by_tags_error_messages = {
    'FormatError': 'Invalid "find-by-tag" format. Command "find-by-tag" must have not less then 2 arguments: <find-by-tag tag1,tag2,tag3>.{RESET}',
}

show_all_error_messages = {
    'FormatError': f'{RED}Contacts are empty. Please, use "add" command to add new contacts.{RESET}',
}

show_all_notes_error_messages = {
    'FormatError': f'{RED}Notes are empty. Please, use "add_note" command to add new notes.{RESET}',
}

show_all_birthdays_error_messages = {
    'FormatError': f'{RED}Invalid "birthdays" format. Command "birthdays" must have 2 arguments: <birthdays per_days>.{RESET}',
    'KeyError': f'{RED}Contacts are empty. Please, use "add" command to add new contacts first.{RESET}',
    'ValidationError': invalid_per_days_error_message,
}

parse_input_error_messages = {
    'FormatError': generic_invalid_command_format_message,
}

change_title_error_messages = {
    'FormatError': f'{RED}Note with provided ID does not exist{RESET}'
}

change_content_error_messages = {
    'FormatError': f'{RED}Note with provided ID does not exist{RESET}'
}

add_tag_error_messages = {
    'FormatError': f'{RED}Note with provided ID does not exist{RESET}'
}

change_tag_error_messages = {
    'FormatError': f'{RED}Invalid "change-tag" format. Command "change-tag" must have at least 2 arguments: <change-tag Tag_value1 tag_value2>.{RESET}',
    'KeyError': f'{RED}Note with provided ID does not exist{RESET}'
}

change_phone_error_messages = {
    'FormatError': f'{RED}Phone number not found in the record{RESET}',
    'KeyError': f'{RED}Such name is not found, please, try again{RESET}'
}

delete_phone_error_messages = {
    'FormatError': f'{RED}Phone number not found in the record{RESET}',
    'KeyError': f'{RED}Such name is not found, please, try again{RESET}'
}

delete_note_error_messages = {
    'FormatError': f'{RED}Invalid "delete-note" format. Command "delete-note" must have 2 arguments: <delete-note ID.{RESET}',
    'KeyError': f'{RED}Such note with provided ID does not exist.{RESET}'
}

delete_contact_error_messages = {
    'FormatError': 'Contact not found in the record',
    'KeyError': 'Such name is not found, please, try again'
}
