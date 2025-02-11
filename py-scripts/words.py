import os
import sys

def get_file_size_words(file_path):
    
    try:
        number_of_words = 0
        with open(file_path, 'r') as file:
            data = file.read()
            lines = data.split()
            number_of_words += len(lines)
        print(f"Number of words: {number_of_words} words")
        print(number_of_words, '     ', file_path)
        return number_of_words
    except FileNotFoundError:
        print(f"File not found {file_path}")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_file_size_words(sys.argv[1])
    else:
        print("No file path provided") 