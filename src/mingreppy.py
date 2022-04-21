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

class Config:
    def __init__(self, args):
        if len(args) < 3:
            print("Not enough arguments")
            sys.exit()
        self.query = args[1]
        self.filename = args[2]    

def run(config):
    try:
        with open(config.filename, 'r') as f:
            print("With text:")
            # print lines to stdout. Omit last new line character
            for line in f.readlines():
                print(line[:len(line)-1])
    except Exception as Err:
        print("Error opening file: `" + config.filename + "`", Err)


def main():
    # function to parse cmd line arguments
    config = Config(sys.argv)
    print("Searching for `" + config.query + "`")
    print("In file `" + config.filename + "`")
    run(config)

if __name__ == '__main__':
    main()
