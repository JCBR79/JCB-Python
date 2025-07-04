import datetime


now= datetime.datetime.now()
future_date = now+datetime.timedelta(days=7)
print(f"7 days from now:{future_date}")

# sustract 3 hours

past_time= now-datetime.timedelta(hours=3)
print(f"3 hours ago: {past_time}")

#calculate the difference between two date times
date1 = datetime.datetime(2024,1,1)
date2= datetime.datetime(2024, 7, 11)
difference= date2-date1
print(f"Differance between 2 days :{difference}")
print(f"Difference in days: {difference.days}")