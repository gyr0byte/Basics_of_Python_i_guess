import os
from datetime import datetime 

print(os.getcwd())  # Get the current working directory
# print(os.listdir())  # Get the list of all the files in the current directory

# os.makedirs('OS_module2') # this will create a folder in the current directory

os.rename('OS_Module', 'os_module') # (original name, changed name)
modified_time = os.stat('Loops').st_mtime

print(datetime.fromtimestamp(modified_time))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print(f"Current Path: {dirpath}")
    print(f"Directories: {dirnames}")
    print(f"Files: {filenames}\n")
