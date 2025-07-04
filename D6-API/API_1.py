import requests
import json
import pandas as pandas
import datetime
import time
import schedule

API_URL= "http://api.open-notify.org/iss-now.json"
REPORT_FILE= "iss_location_report.csv"

def fetch_iss_location():
    """Fetches the current ISS location from  the Open-Notify API"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status() # Raise an exception for HTTP 
        data = response.json()
        print(f" {data}")
        return data
    except requests.exceptions.RequestException as e:
        print(f" Error fetching data from API: {e}")
        return None
fetch_iss_location()

def generate_report_entry():
    iss_data= fetch_iss_location()
    
    if iss_data:
        timestamp= datetime.datetime.fromtimestamp(iss_data['timestamp'])
        latitude = iss_data['iss_position']['latitude']
        longitude = iss_data['iss_position']['longitude']
        print(f"Time is : {timestamp}")
        print(f"latitude is: {latitude}")
        print(f"Longitude is: {longitude}")

generate_report_entry()

import time

for i in range(5):
    print(f"\n🔄 Run {i + 1}")
    generate_report_entry()
    time.sleep(1)  # Wait 1 second between runs