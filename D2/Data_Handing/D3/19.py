import datetime

#Create a date onject
my_date= datetime.date(2023,10,27)
print(f"My date: {my_date}")

#Create a time object (hour, minute, second, microsecond)
my_time= datetime.time(14, 30, 25, 123456)
print(f"My time: {my_time}")

#Create a date time object
my_datetime=datetime.datetime(2024, 5, 23, 6, 15, 34, 166666)
print(f"My datetime: {my_datetime}")