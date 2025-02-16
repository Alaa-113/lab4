from datetime import datetime
def get_date(prompt):
    date_str = input(prompt)
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

date1 = get_date("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = get_date("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

time_difference = date2 - date1
difference_in_seconds = time_difference.total_seconds()

print(f"The difference between the two dates is {difference_in_seconds} seconds.")
