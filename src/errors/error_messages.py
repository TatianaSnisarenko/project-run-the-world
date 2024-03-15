from src.errors.errors import ValidationError

generic_error_message = 'Something went wrong, please try again.'
invalid_phone_number_error_message = 'Invalid phone number: must be 10 digits value.'
invalid_birthday_format_error_message = 'Invalid birthday format: must be <DD.MM.YYYY>.'
invalid_name_format_error_message = 'Invalid name format: name must not be empty.'
invalid_note_id_format_error_message = 'Invalid note id: id must not be a valid number.'
tag_already_exists_error_message_template = 'Such tag: [{tag}] is already present for the note with id: [{id}]'
tag_doenst_exist_error_message_template = 'Such tag: [{tag}] is not found for the note with id: [{id}]'
empty_notes_error_message = 'Notes are empty, please add new notes first'
invalid_email_error_message_template = 'Not a valid email provided: [{email}]. Please try again'
invalid_per_days_error_message = 'Invalid value: must be only numbers from 1 to 365'
empty_notes_error_message = 'Notes are empty. Please, use "add-note" command to add new notes.'

generic_invalid_command_format_message = '''Invalid "command" format. 
Please use <help> to display
all available commands'''

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
change_address_error_messages = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_address>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.'
}

change_contact_error_messages = {
    'FormatError': 'Invalid "change" format. Command "change" must have 3 arguments: <change Name new_phone_number>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.',
    'ValidationError': invalid_phone_number_error_message
}

change_birthday_error_messages = {
    'FormatError': 'Invalid "change-birthday" format. Command "change-birthday" must have 3 arguments: <change-birthday Namenew_birthday>.',
    'KeyError': 'Such name is not found, please, use "add" command instead.',
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
    'FormatError': 'Invalid "show-contact" format. Command "show-contact" must have 2 arguments: <show-contact Name>.',
    'KeyError': 'Such name is not found, please, try again.'
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
    'FormatError': 'Invalid "find-by-tag" format. Command "find-by-tag" must have not less then 2 arguments: <find-by-tag tag1,tag2,tag3>.',
}

show_all_error_messages = {
    'FormatError': 'Contacts are empty. Please, use "add" command to add new contacts.',

}

show_all_notes_error_messages = {
    'FormatError': 'Notes are empty. Please, use "add_note" command to add new notes.',
}

show_all_birthdays_error_messages = {
    'FormatError': 'Invalid "birthdays" format. Command "birthdays" must have 2 arguments: <birthdays per_days>.',
    'KeyError': 'Contacts are empty. Please, use "add" command to add new contacts first.',
    'ValidationError': invalid_per_days_error_message,


}

parse_input_error_messages = {
    'FormatError': generic_invalid_command_format_message,
}

change_title_error_messages = {
    'FormatError': 'Note with provided ID does not exist'
}

change_content_error_messages = {
    'FormatError': 'Note with provided ID does not exist'
}

add_tag_error_messages = {
    'FormatError': 'Note with provided ID does not exist'
}

change_tag_error_messages = {
    'FormatError': 'Note with provided ID does not exist'
}

change_phone_error_messages = {
    'FormatError': 'Phone number not found in the record',
    'KeyError': 'Such name is not found, please, try again'
}

delete_phone_error_messages = {
    'FormatError': 'Phone number not found in the record',
    'KeyError': 'Such name is not found, please, try again'
}

delete_contact_error_messages = {
    'FormatError': 'Contact not found in the record',
    'KeyError': 'Such name is not found, please, try again'
}
