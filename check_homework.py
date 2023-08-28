from datetime import date, timedelta
from main import get_birthdays_per_week

# Test cases
def run_tests():
    users = [
        {"name": "Bill", "birthday": date.today()},
        {"name": "Jan", "birthday": date.today() + timedelta(days=1)},
        {"name": "Kim", "birthday": date.today() + timedelta(days=2)},
    ]

    expected_result = {
        'Monday': ['Bill'],
        'Tuesday': ['Jan'],
        'Wednesday': ['Kim'],
        'Thursday': [],
        'Friday': []
    }

    result = get_birthdays_per_week(users)

    if result == expected_result:
        print("Test passed")
    else:
        print("Test failed")

if __name__ == "__main__":
    run_tests()