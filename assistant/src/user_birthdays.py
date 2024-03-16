from datetime import datetime, timedelta
from collections import defaultdict
from calendar import isleap


def get_birthdays_per_week(users: list, per_days: int) -> tuple:
    """Returns a tuple containing upcoming birthdays of users within a specified number of days.

    Args:
        users (list) : list of dictionaries that contain name:str and birthday: datetime
        example: [{'name': 'Gandalf', 'birthday': record.birthday.birth_date}]
        per_days (int): The number of days within which to search for upcoming birthdays.

    Returns:
        tuple: A tuple containing upcoming birthdays of users within the specified number of days.
    """
    if not users:
        return tuple()
    return get_birthdays_per_week_from_date(users, datetime.today(), per_days)


def get_birthdays_per_week_from_date(users: list, from_date: datetime, per_days: int) -> tuple:
    """Returns upcoming birthdays of users within a specified number of days from a given date.

    Args:
        users (list): A list of dictionaries containing user data with 'name' and 'birthday' keys.
        from_date (datetime.date): The reference date from which to calculate upcoming birthdays.
        per_days (int): The number of days within which to search for upcoming birthdays.

    Returns:
        list: A list of dictionaries containing 'Birthday' and 'Name' keys, representing upcoming birthdays within the specified number of days from the reference date.
    """
    date = from_date.date()

    result = defaultdict(list)

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        birthday_this_year = get_date(date.year, birthday.month, birthday.day)
        delta_days = (birthday_this_year - date).days

        # if birthday less than today, consider next year's birthday.
        if delta_days < 0:
            birthday_this_year = get_date(
                date.year+1, birthday.month, birthday.day)

        # re-establish delta
        delta_days = (birthday_this_year - date).days
        birthday_week_day = birthday_this_year.weekday()

        # check delta should be within a week from today
        if delta_days < int(per_days):
            result[birthday_this_year].append(name)
    ordered_dict = dict(sorted(result.items()))
    formatted_list = []
    for key, value in ordered_dict.items():
        formatted_list.append(
            f'{key.strftime("%d.%m.%Y")}: {", ".join(value)}')
    formatted_l = []
    for key, value in ordered_dict.items():
        formatted_l.append({'Birthday': key.strftime(
            "%d.%m.%Y"), 'Name': ", ".join(value)})
    return formatted_l


def show_birthdays_per_week_from_date(users_birthdays: tuple) -> None:
    """Prints the upcoming birthdays of users within a week from a given date.

    Args:
        users_birthdays (list): A list of dictionaries containing 'Birthday' and 'Name' keys, representing upcoming birthdays of users within a week from a specified date.
    """
    for value in users_birthdays:
        print(value)


def get_date(year: int, month: int, day: int) -> datetime.date:
    """Returns a date object for the given year, month, and day.

    If the given year is not a leap year and the month is February with a day of 29, the day is adjusted to 1st of March.

    Args:
        year (int): The year.
        month (int): The month (1-12).
        day (int): The day of the month.

    Returns:
        datetime.date: A date object representing the given date.
    """
    if not isleap(year) and month == 2 and day == 29:
        month = 3
        day = 1
    return datetime(year, month, day).date()
