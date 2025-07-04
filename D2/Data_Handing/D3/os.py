import os
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")
new_directory = "/tmp"
print(os.path.basename)
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory)
    print(f"changed directory to :{os.getcwd()}")
else:
    print(f"Directory '{new_directory}' doesn not exist or its not a directory")