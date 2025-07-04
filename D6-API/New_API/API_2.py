import requests
import json

BASE_URL = "http://localhost:8000/tasks"

def get_tasks_by_status(status):
    """Fetches and prints tasks filtered by soecific status."""
    print(f"---Getting tasks with Status : '{status}' ---")
    params= {status}

def bulk_create_tasks(num_tasks=5):
    "Creates a specified number of new tasks."""
    print(f" --- Bulk creating {num_tasks} nea tasks---")
    for i in range (num_tasks):
        task_data = {
            "title" : f"Auto-generated Task {i+1}", 
            "description" : f"This is an automated task number {i+1}"
            "status": "pending",
            "dueDate": f"2025-07-{20+i:02d}"
        }
try:
    response = requests.post(BASE_URL, json=task_data)
    response.raise_for_status()
    created_task=response.json()
    print(f" Created Task {i+1}: {created_task['title']}")
except requests.exceptions.RequestException as e:\
print(f" Error creating task {i+1}:{e}")
    