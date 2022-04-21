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
from greppylib import Config, run

def main():
    # function to parse cmd line arguments
    config = Config(sys.argv)
    print("Searching for `" + config.query + "`")
    print("In file `" + config.filename + "`")
    run(config)

if __name__ == '__main__':
    main()
