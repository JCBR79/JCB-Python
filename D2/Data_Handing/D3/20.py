import datetime
now= datetime.datetime.now()
formatted_date_time=now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted datetime: {formatted_date_time}")

fortmatted_date=now.strftime("%A, %B, %d,%Y")
print(f"Formatted Date: {fortmatted_date}")

formatted_time=now.strftime("%I:%M %p") #12 hour formate
print(f"Formatted time: {formatted_time}")

