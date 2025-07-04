import csv
csv_file_name = "emplyees.csv"
target_department= "IT Support"
print("Attempting to read employee data from '{csv_file_name}' and filtyer by '{target_department}'")
filtered_employees = []
try:
    with open(csv_file_name, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row.get('Department')==target_department:
                filtered_employees.append(row)
    print(f"\n---Employees in the '{filtered_employees}' Department ---")
except FileNotFoundError:
    print(f"Error: The file '{csv_file_name}' was not found")
except Exception as e:
    print(f"An unexpected error occured : {e}") 