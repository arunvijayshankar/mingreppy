
import sys
import os

class Config:
    def __init__(self, args):
        if len(args) < 3:
            print("Not enough arguments")
            sys.exit()
        self.query = args[1]
        self.filename = args[2]
        self.case_sensitive = False if os.getenv('CASE_INSENSITIVE') else True

def run(config):
    contents = list()
    try:
        with open(config.filename, 'r') as f:
            print("With text:")
            # print lines to stdout. Omit last new line character
            for line in f.readlines():
                contents.append(line)
        if config.case_sensitive:
            for res in search(config.query, contents):
                print(res.strip('\n'))
        else:
            for res in search_case_insensitive(config.query, contents):
                print(res.strip('\n'))

    except Exception as Err:
        print("Error opening file: `" + config.filename + "`", Err)

def search(query, contents):
    results = list()

    for line in contents:
        if query in line:
            results.append(line)

    print(results)
    return results

def search_case_insensitive(query, contents):
    results = list()

    for line in contents:
        if query.lower() in line.lower():
            results.append(line)
    print(results)
    return results