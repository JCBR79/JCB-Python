import os
file_to_delete = "my_temp_file.txt"
with open(file_to_delete, 'w') as f:
    f.write("This is a temporary file.")
try:
    os.remove(file_to_delete)
    print(f"file '{file_to_delete}' removed successfully.")
except FileNotFoundError:
    print(f"File '{file_to_delete}' does not exist")
except Exception as e:
    print(f"An error occured: {e}")
    