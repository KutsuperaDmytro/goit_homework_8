from datetime import date, timedelta
import time
def get_birthdays_per_week(users):
    today = date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    birthdays_per_week = {weekday: [] for weekday in weekdays}

    for user in users:
        name = user['name']
        birthday = user['birthday']

        next_birthday = date(today.year, birthday.month, birthday.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1, birthday.month, birthday.day)

        weekday_index = next_birthday.weekday()
        weekday = weekdays[weekday_index]

        birthdays_per_week[weekday].append(name)

    return birthdays_per_week

if __name__ == "__main__":
    today = date.today()  # Define 'today' before using it
    users = [
        {"name": "Bill", "birthday": date(today.year, 8, 30)},
        {"name": "Jan", "birthday": date(today.year, 8, 31)},
        {"name": "Kim", "birthday": date(today.year, 9, 1)},
    ]

    birthdays = get_birthdays_per_week(users)
    for weekday, names in birthdays.items():
        print(f"{weekday}: {names}")

    for user in users:
        name = user['name']
        birthday = user['birthday']

        birthday_timestamp = time.mktime(birthday.timetuple())
        today_timestamp = time.mktime(today.timetuple())

        if birthday_timestamp >= today_timestamp:
            days_until_birthday = int((birthday_timestamp - today_timestamp) / (60 * 60 * 24))
            print(f"{name}'s birthday is in {days_until_birthday} days.")
        else:
            print(f"{name}'s birthday has already passed this year.")