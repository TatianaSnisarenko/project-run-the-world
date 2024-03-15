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
                      ' sort-by-tag <tag> <tag>',
                      ' show-note <ID>',
                      ' delete-note <ID>',
                      ' add-note',
                      ' notes',
                      ' exit',
                      ' close',
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
                      'sort-by-tag <tag> <tag>',
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
                      'add-tag <ID> <tag_value>'
                      ]

commands_description = [

    {"Format": "close",
     "Action": "say Gandalf bye",
     "Example": "close"},

    {"Format": "add-contact <Name, other>",#+
     "Action": "add new contact",
     "Example": "add-contact Gandalf 1234567890"},

    {"Format": "delete-contact <Name>",#+
     "Action": "delete the contact",
     "Example": "delete-contact Smaug"},

     {"Format": "contacts",#+
    "Action": "look the contacts",
    "Example": "contacts"},

    {"Format": "show-contact <Name>",#+
    "Action": "look the contact",
    "Example": "show-contact Gimli"},

    {"Format": "add-note <title> <text> <tags>",#+
     "Action": "add note with tegs",
    "Example": "add-note Memo Win Balrog monsters"},

    {"Format": "notes",#+
     "Action": "look the notes list",
    "Example": "notes"},

    {"Format": "change-phone <Name> <old> <new>", #+
    "Action": "change phone",
    "Example": "change-phone Arwen 0736756464 0988888888"},

    {"Format": "add-birthday <Name> <DD.MM.YYYY>",#+
    "Action": "add birthday",
    "Example": "add-birthday Gandalf 01.01.1903"},

    {"Format": "birthdays <per_days>",#+
     "Action": "look birthdays for the period",
    "Example": "birthdays 7"}, 

    {"Format": "change-birthday <Name> <new_date>",#+
    "Action": "change friends birthday",
    "Example": "change-birthday Gandalf 24.09.1903"},

    {"Format": "change-email <Name> <new_email>",#+
     "Action": "change email",
     "Example": "change-email Frodo fred@zlot.ua"},

    {"Format": "change-address <Name> <new_address>", #+
     "Action": "change address",
     "Example": "change-address Frodo Gondolin"},

    {"Format": "change-title <ID> <new_title>", #+
     "Action": "change notes title ",
     "Example": "change-title 1 Plan"},

    {"Format": "add-tag <ID> <tag>", #+
     "Action": "add the tag ",
     "Example": "add-tag 2 orcs"},

    {"Format": "change-tag <ID> <old_tag> <new_tag>", #+
     "Action": "change the tag ",
     "Example": "change-tag 2 orcs goblins"},

    {"Format": "change-content <ID> <new_content>",#+ 
     "Action": "change the notes text ",
     "Example": "change-content 1 Kill Sauron"},

    {"Format": "find-by-phone <Phone>",#+
    "Action": "find the phone",
    "Example": "find-by-phone 0665556666"},

    {"Format": "find-by-email <email>",
     "Action": "find email",
     "Example": "find-by-email frodo@bag.ua"},#+

    {"Format": "find-by-address <address>", 
     "Action": "find by address",
     "Example": "find-by-address Hobitland"},#+

    {"Format": "find-by-birthday <DD.MM.YYYY>",
    "Action": "find by friends birthday",
    "Example": "find-by-birthday 01.05.1905"}, #+

    {"Format": "find-by-title <title>", #+
     "Action": "find by notes title ",
     "Example": "find-by-title Memo"},

    {"Format": "find-by-tag <tag>", #+
     "Action": "find by tag ",
     "Example": "find-by-tag orcs"},

    {"Format": "find-by-content <text>",#+ 
     "Action": "find the notes text ",
     "Example": "find-by-content Kill Sauron"},

    {"Format": "sort-by-tag", #+
     "Action": "sort by tag",
     "Example": "sort-by-tag"},

    {"Format": "show-note <ID>",#+
     "Action": "look the note",
    "Example": "show-note 2"},

    {"Format": "delete-note <note>",#+
     "Action": "look the note",
    "Example": "delete-note Kill Sauron"},

]