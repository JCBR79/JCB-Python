import os
path1 = "C:\JCB-Python/my_existing_file.txt"
path2 = "C:\JCB-Python"
Path3 = "non_existant_path"

print(f"'{path1}' is a file: {os.path.isfile(path1)}")
print(f"'{path1}' is a directory: {os.path.isdir(path1)}")
print(f"'{path2}' is a file: {os.path.isfile(path2)}")
print(f"'{path2}' isa a diectrory:{os.path.isdir(path2)}")