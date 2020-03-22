"""Find a video at the Internet Archive
by a partial title match and display it."""

import sys
import webbrowser
import requests

def search(title):
    """Return a list of 3-item tuples (identifier,
       title, description) about videos
       whose titles partially match :title."""
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": "title:({}) AND mediatype:(movies)".format(title),
        "fl": "identifier,title,description",
        "output": "json",
        "rows": 10,
        "page": 1,
        }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc["identifier"], doc["title"], doc["description"])
            for doc in data["response"]["docs"]]
    return docs

def choose(docs):
    """Print line number, title and truncated description for
    each tuple in :docs. Get the user to pick a line
    number. If it's valid, return the first item in the
    chosen tuple (the "identifier"). Otherwise, return None."""
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}...")
    index = input(f"Which would you like to see (0 to {last})? ")
    try:
        return docs[int(index)][0]
    except:
        return None

def display(identifier):
    """Display the Archive video with :identifier in the browser"""
    details_url = "https://archive.org/details/{}".format(identifier)
    print("Loading", details_url)
    webbrowser.open(details_url)

def main(title):
    """Find any movies that match :title.
       Get the user's choice and display it in the browser."""
    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("Nothing selected")
    else:
        print("Nothing found for", title)

if __name__ == "__main__":
    main(sys.argv[1])
