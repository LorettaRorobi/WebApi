from datetime import datetime
months = {
    'January': 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def parse_month(month_num):
    month = str(month_num).capitalize()
    if month in months.keys():
        return months[month]
    else:
        return None