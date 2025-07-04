import os
path_component1= "C://JCB-Python/OsAndFiles"
path_component2= "/tmp"
file_name = "/monthly_report.pdf"
full_path = os.path.join(path_component1, path_component2, file_name)
print(f"Joined path: {full_path}")
