# Cli Bot assistance for managing contacts and notes

## Description

Our **Assistant Bot** is a user-friendly console bot that you can use to conveniently **manage your contacts** by adding their name, phone, address, email, and birthday. All the data can be modified or deleted at any time. The bot will help you to **remember the birthdays** of your loved ones, colleagues, and acquaintances and even prepare for these dates in advance: simply enter command _birthdays_ with the number of days, and the bot will show you all the birthdays during the period you entered (starting from now). You can also **save your notes** in the bot and find them by title, content, or tag.

## Commands

| **Command**                         | **Action**                            | **Example**                              |
| ----------------------------------- | ------------------------------------- | ---------------------------------------- |
| close                               | save my secrets and exit              | close                                    |
| exit                                | save my secrets and exit              | exit                                     |
| add-contact                         | add new contact, use 'b' to interrupt | add-contact Gandalf 1234567890           |
| delete-contact <Name>               | delete the contact                    | delete-contact Smaug                     |
| contacts                            | show the contacts                     | contacts                                 |
| show-contact <Name>                 | show the contact                      | show-contact Gimli                       |
| add-note <note>                     | add new note, use 'b' to interrupt    | add-note                                 |
| notes                               | show the notes list                   | notes                                    |
| change-phone <Name> <old> <new>     | update phone for contact              | change-phone Arwen 0736756464 0988888888 |
| add-birthday <Name> <DD.MM.YYYY>    | add birthday for contact              | add-birthday Gandalf 01.01.1903          |
| birthdays <per_days>                | show birthdays for the period         | birthdays 7                              |
| change-birthday <Name> <new_date>   | update contact's birthday             | change-birthday Gandalf 24.09.1903       |
| change-email                        | change email for contact              | change-email Frodo                       |
| change-address                      | change address for contact            | change-address Gandalf                   |
| change-title                        | change notes title                    | change-title 1                           |
| add-tag <ID> <tag>                  | add tag for note                      | add-tag 2 orcs                           |
| change-tag <ID> <old_tag> <new_tag> | replace old tag with new one          | change-tag 2 orcs goblins                |
| change-content <ID> <new_content>   | change the note's text                | change-content 1 Kill Sauron             |
| find-by-phone <Phone>               | find contact by phone                 | find-by-phone 0665556666                 |
| find-by-email <email>               | find contact by email                 | find-by-email frodo@bag.ua               |
| find-by-address <address>           | find contact by address               | find-by-address Hobitland                |
| find-by-birthday <DD.MM.YYYY>       | find contact by birthday              | find-by-birthday 01.05.1905              |
| find-by-title <some_title>          | find contact by title                 | find-by-address Memo                     |
| find-by-tag <tag>                   | find note by tag                      | find-by-tag orcs                         |
| find-by-content <text>              | find note by content                  | find-by-content Kill Sauron              |
| sort-by-tag                         | sort notes by tags                    | sort-by-tag                              |
| show-note <ID>                      | show the note by id                   | show-note 2                              |
| delete-note                         | delete note by Id                     | delete-note 1                            |

## Steps to start the project using main:

1. Move to folder that contains requirements.txt and run command in terminal:

   Windows

   ```
   pip install -r requirements.txt
   ```

   Mac

   ```
   pip3 install -r requirements.txt
   ```

2. Run main.py

## Steps to start the project from terminal:

1. Run command in terminal:

   Windows

   ```
   pip install setuptools
   ```

   Mac

   ```
   pip3 install setuptools
   ```

2. Move to folder that contains setup.py and run command in terminal:

   Windows

   ```
   pip install .
   ```

   Mac

   ```
   pip3 install .
   ```

3. Use start command to run assistant in terminal:

   Windows, Mac

   ```
   run_bot
   ```
