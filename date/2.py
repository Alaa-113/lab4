import datetime
from datetime import timedelta
current_date=datetime.datetime.today()
tomorrow =current_date + timedelta(days=1)
yesterday =current_date - timedelta(days=1)
print("yesterday was", yesterday.strftime('%d-%m-%Y'))
print("today is", current_date.strftime('%d-%m-%Y'))
print("tomorrow is", tomorrow.strftime('%d-%m-%Y'))