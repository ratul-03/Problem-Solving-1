import os

# Function to print contents of a directory
def print_directory_contents(path):
    try:
        # List all the files and directories in the given path
        directory_contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in directory_contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
directory_path = '/'  # Current directory
print_directory_contents(directory_path)
