

RED = "\33[31m"
BRED = '\033[1;38;5;196m'
GREEN = "\033[32m"
RESET = "\033[0m"

generic_error_message = (f'''{RED}
You Shall Not Pass. {RESET}
{BRED}Something went wrong, please try again.
{RESET}''')
invalid_phone_number_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid phone number: must be 10 digits value.
{RESET}''')
invalid_birthday_format_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid birthday format: must be <DD.MM.YYYY>.
{RESET}''')
invalid_name_format_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid name format: name must not be empty.
 {RESET}''')
invalid_note_id_format_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid note id: id must be a valid number.
{RESET}''')
tag_already_exists_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Such tag: is already present for the note with id.
{RESET}''')
tag_doenst_exist_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Such tag: is not found for the note with id.
{RESET}''')
note_doesnt_exist_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Note with provided ID does not exist.
{RESET}''')
invalid_email_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Not a valid email provided. Please try again
                                        {RESET}''')
invalid_per_days_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid value: must be only numbers from 1 to 365.
 {RESET}''')
empty_notes_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Notes are empty. Please, use "add-note" command to add new notes.
{RESET}''')

empty_notes_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Notes are empty, please add new notes first
{RESET}''')
invalid_email_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Not a valid email provided. Please try again
                                        {RESET}''')
invalid_per_days_error_message = (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid value: must be only numbers from 1 to 365.
{RESET}''')
empty_notes_error_message = (f'''{RED}
You have no Power here. {RESET}
{BRED}Notes are empty. Please, use "add-note" command to add new notes.
{RESET}''')

generic_invalid_command_format_message = (f'''{RED}
My dear friend, be carefull!
You've enterd command in invalid format.{RESET}
{BRED}Please use <help> to display all available commands{RESET}
{RED}I've prepeared for you
{RESET}''')

add_note_error_messages = {
    'FormatError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note is already present, please, use "change" command instead.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note is already present, please, use "change-note" command instead.
{RESET}''')
}

change_note_title_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-title" format. Command "change-title" must have 2 arguments: <change-title ID>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note is apsent, please, use "add-note" command instead.
{RESET}''')
}

change_note_content_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-content" format. Command "change-content" must have 2 arguments: <change-content ID>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note is apsent, please, use "add-note" command instead.
{RESET}''')
}

show_note_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "show-note" format. Command "show-note" must have 2 arguments: <show-note ID>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note with provided ID does not exist.
{RESET}''')
}

add_birthday_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "add-birthday" format. Command "add-birthday" must have 3 arguments: <add-birthday Name DD.MM.YYYY>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, use "add" command to add new contact first.
{RESET}''')
}

add_contact_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "add" format. Command "add" must have 3 arguments: <add Name phone_number>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is already present, please, use "change" command instead.
                 {RESET}''')
}
change_address_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change" format. Command "change" must have 3 arguments: <change Name new_address>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, use "add" command instead.
{RESET}''')
}

add_tag_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "add-tag" format. Command "add-tag" must have 2 arguments: <add-tag Tag_value>.
                    {RESET}'''),
    'KeyError': note_doesnt_exist_error_message
}

change_phone_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-phone" format. Command "change-phone" must have 3 arguments: <change-phone Name old_phone new_phone>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name with such phone is not found, please, use "add" command instead.
                 {RESET}''')
}

delete_phone_error_messages = {
    'FormatError': f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "delete-phone" format. Command "delete-phone" must have 3 arguments: <delete-phone Name phone>.
{RESET}''',
    'KeyError': f'''{RED}
You have no Power here. {RESET}
{BRED}Such name with such phone is not found, please, check your input.
{RESET}'''
}

add_phone_error_messages = {
    'FormatError': f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "add-phone" format. Command "add-phone" must have 3 arguments: <add-phone Name phone>.
{RESET}''',
    'KeyError': f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, check your input.
{RESET}'''
}

change_birthday_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-birthday" format. Command "change-birthday" must have 3 arguments: <change-birthday Namenew_birthday>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, use "add" command instead.
{RESET}''')
}

change_email_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-email" format. Command "change-email" must have 3 arguments: <change-email  Name  new_email>.
{RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, use "add" command instead.
{RESET}''')
}


show_phone_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.
                    {RESET}'''),
}

show_contact_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "show-contact" format. Command "show-contact" must have 2 arguments: <show-contact Name>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.
                 {RESET}''')
}

show_phone_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "phone" format. Command "phone" must have 2 arguments: <phone Name>.
    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.
                 {RESET}''')
}

sort_by_tags_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.
Invalid "sort-by-tag" format. Command "sort-by-tag" must have 1 arguments: <find-by-tag>.
{RESET}'''),
}

find_by_tags_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-tag" format. Command "find-by-tag" must have not less then 2 arguments: <find-by-tag tag1,tag2,tag3>.
                    {RESET}''')
}

find_by_title_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.
Invalid "find-by-title" format. Command "find-by-title" must have 2 arguments: <find-by-title title>.
{RESET}'''),
}

find_by_content_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.
Invalid "find-by-content" format. Command "find-by-content" must have 2 arguments: <find-by-content content>.
{RESET}'''),
}

find_by_phone_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-phone" format. Command "find-by-phone" must have 2 arguments: <find-by-phone Phone>.
                    {RESET}'''),
    'KeyError':  (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.
                  {RESET}''')
}

find_by_birthday_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-phone" format. Command "find-by-phone" must have 2 arguments: <find-by-phone Phone>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.
                 {RESET}''')
}

find_by_email_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-email" format. Command "find-by-email" must have 2 arguments: <find-by-phone Email>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.
                 {RESET}''')
}

find_by_address_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-address" format. Command "find-by-address" must have 2 arguments: <find-by-address Email>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again.{RESET}''')
}

find_by_tags_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "find-by-tag" format. Command "find-by-tag" must have not less then 2 arguments: <find-by-tag tag1,tag2,tag3>.
                    {RESET}'''),
}

show_all_error_messages = {
    'FormatError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Contacts are empty. Please, use "add" command to add new contacts.
                    {RESET}'''),
}

show_all_notes_error_messages = {
    'FormatError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Notes are empty. Please, use "add_note" command to add new notes.
                    {RESET}'''),
}

show_all_birthdays_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "birthdays" format. Command "birthdays" must have 2 arguments: <birthdays per_days>.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Contacts are empty. Please, use "add" command to add new contacts first.
                 {RESET}''')
}

parse_input_error_messages = {
    'FormatError': generic_invalid_command_format_message,
}

change_tag_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-tag" format. Command "change-tag" must have at least 2 arguments: <change-tag Tag_value1 tag_value2>.
                    {RESET}'''),
    'KeyError':  note_doesnt_exist_error_message
}

change_title_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-title" format. Command "change-title" must have 2 arguments: <change-title ID>.
                    {RESET}'''),
    'KeyError':  note_doesnt_exist_error_message
}

change_content_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "change-content" format. Command "change-content" must have 2 arguments: <change-content ID>.
                    {RESET}'''),
    'KeyError': note_doesnt_exist_error_message
}

add_tag_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "add-tag" format. Command "add-tag" must have 3 arguments: <add-tag ID Tag_value>.
                    {RESET}'''),
    'KeyError': note_doesnt_exist_error_message
}

delete_phone_error_messages = {
    'FormatError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Phone number not found in the record
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again
                 {RESET}''')
}

delete_note_error_messages = {
    'FormatError': (f'''{RED}
The language is that of Mordor, which I will not utter here.{RESET}
{BRED}Invalid "delete-note" format. Command "delete-note" must have 2 arguments: <delete-note ID.
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such note with provided ID does not exist.
                 {RESET}''')
}

delete_contact_error_messages = {
    'FormatError': (f'''{RED}
You have no Power here.{RESET}
{BRED}Contact not found in the record
                    {RESET}'''),
    'KeyError': (f'''{RED}
You have no Power here. {RESET}
{BRED}Such name is not found, please, try again
                 {RESET}''')
}
