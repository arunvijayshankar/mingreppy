from greppylib import search, search_case_insensitive

def case_sensitive():
    query = "duct"
    contents = ["Rust:", "safe, fast, productive.", "Pick three.", "Duct tape"]
    results = search(query, contents)

    if not ["safe, fast, productive."] == results:
        print("Test case_sensitive failed. search did not return `safe, fast, productive.`")
        print("results: " + str(results))
    else:
        print("Found `" + query + "` in `" + str(search(query, contents)) + "`")

def case_insensitive():
    query = "rUsT"
    contents = ["Rust:", "safe, fast, productive.", "Pick three.", "Trust me."]
    results = search_case_insensitive(query, contents)

    if not ["Rust:", "Trust me."] == results: 
        print("Test case_insensitive failed. search did not return `[\"Rust:\", \"Trust me\"]`")
        print("results: " + str(results)) 
    else:
        print("Found `" + query + "` in `" + str(results) + "`")

def main():
    case_sensitive()
    case_insensitive()

if __name__ == '__main__':
    main()