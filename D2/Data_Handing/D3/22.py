import datetime

Sri_lanka_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now_sri_lanka = datetime.datetime.now(Sri_lanka_offset)
print(f"Current date time in Sri Lanka: {now_sri_lanka}")