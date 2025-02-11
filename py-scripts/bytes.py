import os
import sys

def get_file_size_bytes(file_path):
    
    try:
        file_size = os.path.getsize(file_path)
        print(f"File size: {file_size} bytes")
        print(file_size, '     ', file_path)  # This should output the number
        return file_size
    except FileNotFoundError:
        print(f"File not found {file_path}")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# Ensure this runs when script is called directly
if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_file_size_bytes(sys.argv[1])
    else:
        print("No file path provided")