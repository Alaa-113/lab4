from datetime import datetime
current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0).time()#to only show the time

print("Original datetime:", current_datetime)
print("Datetime without microseconds:", without_microseconds)
