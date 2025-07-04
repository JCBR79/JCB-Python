import requests
import json

BASE_URL= "http://localhost:8000/tasks"

def partial_update_task(task_id):
    url=f"{BASE_URL}/{task_id}"
    patch_data = {
        "status":"completed"
    }
    try:
        response= requests.patch(url, json=patch_data)
        response.raise_for_status()
        updated_task=response.json()
        print(f"Task {task_id} partially updated sucessfully;")
        print(json.dumps(updated_task, indent= 2))
    except requests.exceptions.HTTPError as e:
        print(f"Error partially updationg task: {e}")
        if e.response.status_code==404:
            print(f"Bad Requests: {e.response.json().get('error', 'Un')}")
    except requests.exceptions.RequestException as e:
        print(f"Error cnnecting to API: {e}")
        print("-" * 30)
partial_update_task("task123")

if __name__ == "__main__":
    partial_update_task("task123")
    partial_update_task("nonexistant_task_for_patch")