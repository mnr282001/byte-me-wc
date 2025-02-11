# 📊 Byte Me WC: Custom Word Count (wc) Tool

## 🚀 Overview
A lightweight, custom implementation of the classic Unix wc command with core functionality for counting bytes, lines, and words.

## ✨ Features
- `-c`: Count bytes in a file
- `-l`: Count lines in a file
- `-w`: Count words in a file

## 🛠 Installation & Setup

### Prerequisites
- Bash
- Python 3.x

### Quick Setup
1. Clone the repository
2. Make the shell script executable:
   ```bash
   chmod +x my-wc.sh

### Usage
1. Source the script:
   ```bash
   source my-wc.sh
   ```
2. Run the wc command:
   ```bash
   my-wc -c <file>
   my-wc -l <file>
   my-wc -w <file>
   ```

### 🔍 Examples

    ```bash
    my-wc -c README.md # Count bytes in a file
    my-wc -l tests/test-1.txt # Count lines in a file
    my-wc -w tests/test-1.txt # Count words in a file
    ```
### 🤝 Contributing
Feel free to open issues or submit pull requests!

