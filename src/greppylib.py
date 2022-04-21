
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