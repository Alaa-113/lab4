import datetime
from datetime import timedelta
current_date=datetime.datetime.today()
substraced_date=current_date - timedelta(days=5)
print("current date" ,current_date.strftime('%d-%m-%Y'))
print("substraced_date", substraced_date.strftime('%d-%m-%Y'))