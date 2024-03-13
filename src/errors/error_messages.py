from src.errors.errors import ValidationError

generic_error_message = 'Something went wrong, please try again.'
invalid_phone_number_error_message = 'Invalid phone number: must be 10 digits value.'
invalid_birthday_format_error_message = 'Invalid birthday format: must be <DD.MM.YYYY>.'
invalid_name_format_error_message = 'Invalid name format: name must not be empty.'
invalid_note_id_format_error_message = 'Invalid note id: id must not be a valid number.'
tag_already_exists_error_message_template = 'Such tag: [{tag}] is already present for the note with id: [{id}]'
tag_doenst_exist_error_message_template = 'Such tag: [{tag}] is not found for the note with id: [{id}]'

generic_invalid_command_format_message = '''Invalid "command" format. Available commands: 
    - <add Name phone_namber> - to add contact, 
    - <change Name new_phone_number> - to update contact,
    - <phone Name> - to show phone for the contact
    - <contacts> - to show all contacts,
    - <hello> - to show assistance message,
    - <add-birthday Name DD.MM.YYYY> - to add birthday for contact,
    - <show-birthday Name> - to show birthday for the contact,
    - <birthdays> - to show all birthdays per working week,
    - <add_note> - to add new note,
    - <notes> - to show all messages,
    - <exit> - to exit the bot,
    - <close> - to close the bot'''

add_note_error_messages = {
    'FormatError': 'Such note is already present, please, use "change_note" command instead.',
    'KeyError': 'Such note is already present, please, use "change_note" command instead.'
}

add_birthday_error_messages = {
    'FormatError': 'Invalid "add-birthday" format. Command "add-birthday" must have 3 arguments: <add-birthday Name DD.MM.YYYY>.',
    'KeyError': 'Such name is not found, please, use "add" command to add new contact first.',
    'ValidationError': invalid_birthday_format_error_message
}

add_contact_error_messages = {
    'FormatError': 'Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.',
    'KeyError': 'Such name is already present, please, use "change" command instead.',
    'ValidationError': invalid_phone_number_error_message
}

change_contact_error_messages = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.',
    'ValidationError': invalid_phone_number_error_message
}

show_phone_error_messages = {
    'FormatError': 'Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.',
    'KeyError': 'Such name is not found, please, try again.'
}

show_birthday_error_messages = {
    'FormatError': 'Invalid "show-birthday" format. Command "show-birthday" must have 2 arguments: <show-birthday Name>.',
    'KeyError': 'Such name is not found, please, try again.'
}

show_all_error_messages = {
    'FormatError': 'Contacts are empty. Please, use "add" command to add new contacts.',
}

show_all_notes_error_messages = {
    'FormatError': 'Notes are empty. Please, use "add_note" command to add new notes.',
}

show_all_birthdays_error_messages = {
    'FormatError': 'Contacts are empty. Please, use "add" command to add new contacts first.'
}

parse_input_error_messages = {
    'FormatError': generic_invalid_command_format_message,
}

change_title_error_messages = {
    'KeyError': 'Note with provided ID does not exist'
}

change_content_error_messages = {
    'KeyError': 'Note with provided ID does not exist'
}

add_tag_error_messages = {
    'KeyError': 'Note with provided ID does not exist'
}

change_tag_error_messages = {
    'KeyError': 'Note with provided ID does not exist'
}

change_phone_error_messages = {
    'ValueError': 'Phone number not found in the record'
}

delete_phone_error_messages = {
    'ValueError': 'Phone number not found in the record'
}