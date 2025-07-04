import csv
#create a list of dictionaris where each disctionary represents ....
employees_data = [ 
    {"Name": "Alice Johnson", "Department": "Engineering", "Salary": 85000},
    {"Name": "Brian Smith", "Department": "Marketing", "Salary": 65000},
    {"Name": "Clara Lee", "Department": "Human Resources", "Salary": 60000},
    {"Name": "David Kim", "Department": "Finance", "Salary": 75000},
    {"Name": "Emily Chen", "Department": "IT Support", "Salary": 58000}
    ]

#Define the names of the CSV file
csv_file_name = "emplyees.csv"

#Define the fiedl names (header) for the CSV file
#These should match the keys in your emplyee dictionaries

Feildnames = ["Name", "Department", "Salary"]
print(f"Attemting to write employee data to 'csv_file_name' ...")
try:
    with open(csv_file_name, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=Feildnames)

        writer.writeheader()
        print("CSV headers written")

        writer.writerows(employees_data)
        print(f"Successfully wrote {len(employees_data)} employees records to {csv_file_name}")

except IOError as e:
    print(f"Error:Could not write to file'{csv_file_name}'. {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")
    