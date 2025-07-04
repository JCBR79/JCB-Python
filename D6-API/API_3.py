import requests
import json
import pandas as pandas
import datetime
import time
import schedule

BASE_URL= "http://localhost:8000/tasks"
REPORT_FILE= "iss_location_report.csv"

def fetch_iss_location():
    """Fetches the current ISS location from  the Open-Notify API"""
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status() # Raise an exception for HTTP 
        data = response.json()
        print("All Tasks:")
        print(json.dumps(data, indent=2))
        return data
    except requests.exceptions.RequestException as e:
        print(f" Error fetching all tasks: {e}")
    print("-"* 30)
fetch_iss_location()