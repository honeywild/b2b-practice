import os

# Define the path to the file containing the list of paths
path_file = 'path_list.txt'

# Define the base directory where you want to recreate the directory tree
base_directory = '/'

# Function to create directories and empty files
def create_directories_and_files(path):
    if path.endswith('/'):
        # It's a directory
        directory_path = os.path.join(base_directory, path)
        os.makedirs(directory_path, exist_ok=True)
    else:
        # It's a file
        file_path = os.path.join(base_directory, path)
        directory = os.path.dirname(file_path)
        os.makedirs(directory, exist_ok=True)
        open(file_path, 'w').close()

# Read the list of paths from the file
with open(path_file, 'r') as file:
    paths = file.read().splitlines()

# Iterate through each path and create directories and files
for path in paths:
    create_directories_and_files(path)

print("Directory tree with empty files restored.")

