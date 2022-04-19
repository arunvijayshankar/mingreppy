"""
a minimal grep tool in python
arguments:
1. Search String
2. File name
Output:
String if found in file,
"{String} not found in text if not"

Usage:
    mingreppy.py <search string> <file name>

"""

import sys

def main():
    query = sys.argv[1]
    filename = sys.argv[2]

    print("Searching for " + query)
    print("In file " + filename)

if __name__ == '__main__':
    main()
