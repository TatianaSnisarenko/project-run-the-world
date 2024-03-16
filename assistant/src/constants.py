available_commands = [' add-contact (press enter)',
                      ' change <Name> <new_phone_number>',
                      ' delete-contact <Name>',
                      ' phone <Name>',
                      ' contacts',
                      ' change-email <Name> <New_Email>',
                      ' change-phone <Name> <Old_Phone> <New_Phone>',
                      ' change-address <Name> <New_Address>',
                      ' hello',
                      ' add-birthday <Name> <DD.MM.YYYY>',
                      ' change-birthday <Name> <DD.MM.YYYY>',
                      ' show-contact <Name>',
                      ' find-by-phone <Phone>',
                      ' find-by-address <Address>',
                      ' find-by-email <Email>',
                      ' find-by-birthday <Birthday>',
                      ' contacts',
                      ' add-birthday <Name> <DD.MM.YYYY>',
                      ' change-birthday <Name> <DD.MM.YYYY>',
                      ' birthdays <per_days>',
                      ' change-tag <ID> <old_tag> <new_tag>',
                      ' find-by-title <title>',
                      ' find-by-content <content>',
                      ' sort-by-tag',
                      ' show-note <ID>',
                      ' delete-note <ID>',
                      ' add-note',
                      ' notes',
                      ' exit',
                      ' close',
                      ' delete-phone <Name> <Phone>'
                      'add-contact (press enter)',
                      'change <Name> <new_phone_number>',
                      'change-email <Name> <New_Email>',
                      'change-phone <Name> <Old_Phone> <New_Phone>',
                      'change-address <Name> <New_Address>',
                      'delete-contact <Name>',
                      'phone <Name>',
                      ' find-by-tag <tag1>,<tag2>,...',
                      ' change-title <ID>',
                      ' change-content <ID>',
                      ' add-tag <ID> <tag_value>'
                      ' help',
                      'change <Name> <new_phone_number>',
                      'contacts',
                      'add-birthday <Name> <DD.MM.YYYY>',
                      'change-birthday <Name> <DD.MM.YYYY>',
                      'show-birthday <Name>',
                      'show-contact <Name>',
                      'find-by-phone <Phone>',
                      'find-by-address <Address>',
                      'find-by-email <Email>',
                      'find-by-birthday <Birthday>',
                      'change-tag <ID> <old_tag> <new_tag>',
                      'find-by-title <title>',
                      'find-by-content <content>',
                      'sort-by-tag',
                      'show-note <ID>',
                      'delete-note <ID>',
                      'show-birthday <Name>',
                      'birthdays <per_days>',
                      'add-note',
                      'notes',
                      'exit',
                      'close',
                      'help',
                      'find-by-tag <tag1>,<tag2>,...',
                      'change-title <ID>',
                      'change-content <ID>',
                      'add-tag <ID> <tag_value>',
                      'delete-phone <Name> <Phone>'
                      ]

commands_description = [

    {"Format": "close",
     "Action": "our secrets are safe with me",
     "Example": "close"},

    {"Format": "add-contact",
     "Action": "add new contact",
     "Example": "add-contact Gandalf 1234567890"},

    {"Format": "delete-contact <Name>",  # +
     "Action": "delete the contact",
     "Example": "delete-contact Smaug"},

    {"Format": "delete-phone <Name> <Phone>",  # +
     "Action": "delete the contact's phone",
     "Example": "delete-phone Smaug 1236547890"},

    {"Format": "contacts",  # +
     "Action": "show the contacts",
     "Example": "contacts"},

    {"Format": "show-contact <Name>",  # +
     "Action": "show the contact",
     "Example": "show-contact Gimli"},

    {"Format": "add-note <note>",  # +
     "Action": "add new note",
     "Example": "add-note"},

    {"Format": "notes",  # +
     "Action": "show the notes list",
     "Example": "notes"},

    {"Format": "change-phone <Name> <old> <new>",  # +
     "Action": "update phone for contact",
     "Example": "change-phone Arwen 0736756464 0988888888"},

    {"Format": "add-birthday <Name> <DD.MM.YYYY>",  # +
     "Action": "add birthday for contact",
     "Example": "add-birthday Gandalf 01.01.1903"},

    {"Format": "birthdays <per_days>",  # +
     "Action": "show birthdays for the period",
     "Example": "birthdays 7"},

    {"Format": "change-birthday <Name> <new_date>",  # +
     "Action": "update contact's birthday",
     "Example": "change-birthday Gandalf 24.09.1903"},

    {"Format": "change-email",  # +
     "Action": "change email for contact",
     "Example": "change-email Frodo"},

    {"Format": "change-address",  # +
     "Action": "change address for contact",
     "Example": "change-address Gandalf"},

    {"Format": "change-title",  # +
     "Action": "change notes title ",
     "Example": "change-title 1"},

    {"Format": "add-tag <ID> <tag>",  # +
     "Action": "add tag for note",
     "Example": "add-tag 2 orcs"},

    {"Format": "change-tag <ID> <old_tag> <new_tag>",  # +
     "Action": "replace old tag with new one",
     "Example": "change-tag 2 orcs goblins"},

    {"Format": "change-content <ID> <new_content>",  # +
     "Action": "change the note's text ",
     "Example": "change-content 1 Kill Sauron"},

    {"Format": "find-by-phone <Phone>",  # +
     "Action": "find contact by phone",
     "Example": "find-by-phone 0665556666"},

    {"Format": "find-by-email <email>",
     "Action": "find contact by email",
     "Example": "find-by-email frodo@bag.ua"},  # +

    {"Format": "find-by-address <address>",
     "Action": "find contact by address",
     "Example": "find-by-address Hobitland"},  # +

    {"Format": "find-by-birthday <DD.MM.YYYY>",
     "Action": "find contact by birthday",
     "Example": "find-by-birthday 01.05.1905"},  # +

    {"Format": "find-by-title <title>",  # +
     "Action": "find note by title",
     "Example": "find-by-title Memo"},

    {"Format": "find-by-tag <tag>",  # +
     "Action": "find note by tag",
     "Example": "find-by-tag orcs"},

    {"Format": "find-by-content <text>",  # +
     "Action": "find note by content",
     "Example": "find-by-content Kill Sauron"},

    {"Format": "sort-by-tag",  # +
     "Action": "sort notes by tags",
     "Example": "sort-by-tag"},

    {"Format": "show-note <ID>",  # +
     "Action": "show the note by id",
     "Example": "show-note 2"},

    {"Format": "delete-note",  # +
     "Action": "delete note by Id",
     "Example": "delete-note 1"},

]
