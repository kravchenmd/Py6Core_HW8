from datetime import datetime, timedelta
import calendar


def congratulate(users: list) -> None:
    '''
    This function outputs names of colleagues whose B-day will be on the next week 
    (from current day) by the day of the week. If B-day is on the Sa or Su of the 
    current week, then congratulation have to be done on Monday.
    If there are no colleagues, it outputs "No colleagues to congratulate"
    '''
    b_day_dict = {}

    today_date = datetime.today()
    # today_date += timedelta(days=1)
    # print(f"Today is {today_date.date()}")

    next_monday_date = today_date + timedelta(days=7 - today_date.weekday())
    # print(f"Next Monday is {next_monday_date.strftime('%d %b %Y')}")

    for user in users:
        user_b_day = user['birthday']
        # print(f"User {user['name']}'s birthday is {user_b_day.date()}")

        # ckeck further only if user's birthday is in this month
        if user_b_day.month == today_date.month:
            # number of days from next monday to user's birthday
            td = user_b_day.day - next_monday_date.day

            if td in range(5):  # if b-day is in the first 5 days of the next week
                w_day = next_monday_date + timedelta(days=td)
                w_day = calendar.day_name[w_day.weekday()]

            elif td in [-1, -2]:  # when b-day is on Sa or Su of the current week
                # congradulations will be sent on next Monday
                w_day = 'Monday'

            else:
                continue

            # initialize item in dict if it doesn't exist
            if not(w_day in b_day_dict):
                b_day_dict.update({w_day: [user['name']]})
            # otherwise append name of the user to the list
            else:
                b_day_dict[w_day].append(user['name'])

    if not b_day_dict:
        print("No colleagues to congratulate")
        return None

    for key, value in b_day_dict.items():
        print(f"{key}: {', '.join(value)}")


if __name__ == "__main__":
    # accordint to the HW description, a birthday is a 'datetime' object
    test_users = [
        {
            "name": "Alex",
            "birthday": datetime(year=1978, month=5, day=16)
        },
        {
            "name": "Bill",
            "birthday": datetime(year=1999, month=5, day=18)
        },
        {
            "name": "Joe",
            "birthday": datetime(year=1999, month=5, day=21)
        },
        {
            "name": "Q",
            "birthday": datetime(year=1999, month=5, day=30)
        },
        {
            "name": "M",
            "birthday": datetime(year=1999, month=5, day=25)
        },
        {
            "name": "Ann",
            "birthday": datetime(year=1999, month=5, day=23)
        },
        {
            "name": "Mike",
            "birthday": datetime(year=1999, month=12, day=25)
        },
        {
            "name": "Rob",
            "birthday": datetime(year=1999, month=5, day=14)
        },
        {
            "name": "Vince",
            "birthday": datetime(year=1999, month=3, day=9)
        }
    ]

    congratulate(test_users)
