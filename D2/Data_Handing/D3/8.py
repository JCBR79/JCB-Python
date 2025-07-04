import os
folder_to_remove="TETS1"
os.mkdir(folder_to_remove)

try:
    os.rmdir(folder_to_remove)
    print(f"Directory '{folder_to_remove}' removed successfully.")
except OSError as e:
    print(f"Error removing directlry.")
