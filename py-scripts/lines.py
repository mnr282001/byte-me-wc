import os
import sys

def get_file_size_lines(file_path):
    
    try:
        with open(file_path, 'r') as fp:
            lines = sum(1 for line in fp)
            print(f'Total Number of lines: {lines} lines')
            print(lines, '     ', file_path)
            return lines
    except FileNotFoundError:
        print(f"File not found {file_path}")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_file_size_lines(sys.argv[1])
    else:
        print("No file path provided")