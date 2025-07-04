import pathlib

# ---1. Creating Path Objects---
print("\n---1. Creating Path Objects---")
#current working directory
print(pathlib.Path)
current_dir = pathlib.Path.cwd()
print(f"Current Working Directory (path object): {current_dir}")

#A relative path
relative_file = pathlib.Path('my_document.txt')
print(f"Relative file Path: {relative_file}")

# An absolute Path 
absolute_path = pathlib.Path('/tmp/test_dir')
print(f"Absolute Path: {absolute_path}")

#joining Paths using the /operator 
jopined_path = current_dir / 'data' / 'reports' / 'reports.csv'
print(f"Joined path using / operator: {jopined_path}")

# ---2. Accessing Path Components---
print("\n---2. Accessing Path Components---")
print(f"Full path: {jopined_path}")
print(f"File/Folder name: {jopined_path.name}")
print(f"Parent Directory: {jopined_path.parent}")
print(f"Filestem(name without suffic): {jopined_path.stem}")# 'report'
print(f"File Suffix (extension): {jopined_path.suffix}")#'.csv'
print(f"All suffixes:{jopined_path.suffixes}")#['csv']
print(f"Anchor(root of the path): {jopined_path.anchor}")# '/' on unix, 'C:\' on windows
print(f"Path parts: {jopined_path.parts}") # ('/', 'path', 'to', ...)
