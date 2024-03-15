from datetime import datetime, timedelta
from collections import defaultdict
from calendar import isleap


def get_birthdays_per_week(users, per_days):
    if not users:
        return tuple()
    return get_birthdays_per_week_from_date(users, datetime.today(), per_days)


def get_birthdays_per_week_from_date(users, from_date, per_days):
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


def show_birthdays_per_week_from_date(users_birthdays):
    for value in users_birthdays:
        print(value)


def get_date(year, month, day):
    if not isleap(year) and month == 2 and day == 29:
        month = 3
        day = 1
    return datetime(year, month, day).date()
