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
    # store cmd line args to variables
    query = sys.argv[1]
    filename = sys.argv[2]

    print("Searching for " + query)
    print("In file " + filename)

    try:
        f = open(filename, 'r')
    except Exception as Err:
        print("Error opening file: " + Err)

    print("With text:")
    # print lines to stdout. Omit last new line character
    for line in f.readlines():
        print(line[:len(line)-1])

if __name__ == '__main__':
    main()
