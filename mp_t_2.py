from datetime import datetime, timedelta
def A(x):
    try:
        formatted_date = datetime.strptime(x, '%a,%d %b %Y %H:%M:%S %Z')
    except ValueError:
        print("Invalid")
    weekend_days = ['Saturday', 'Sunday']
    if formatted_date.strftime('%A') in weekend_days:
        if formatted_date.strftime('%A') == 'Sunday':
            nextday = formatted_date + timedelta(days=1)
            print("Next working day will be : ", nextday.strftime('%Y/%m/%d'))
        else:
            nextday = formatted_date + timedelta(days=2)
            print("Next working day will be : ", nextday.strftime('%Y/%m/%d'))
    else:
        # Return input date
        print(formatted_date.strftime('%Y/%m/%d'))


A("sat,17 Dec 2022 14:30:00 GMT")
