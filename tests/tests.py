from greppylib import search

def one_result():
    query = "duct"
    contents = "Rust:\nsafe, fast, productive.\nPick three."

    if not "safe, fast, productive." == search(query, contents):
        print("Test one_result failed. search did not return `safe, fast, productive.`")
    else:
        print("Found `" + query + "` in `" + search(query, contents) + "`")

def main():
    one_result()

if __name__ == '__main__':
    main()