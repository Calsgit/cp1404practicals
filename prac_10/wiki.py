import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    query = input("Enter page title: ")
    while query != "":
        result = ""
        try:
            result = wikipedia.summary(query, auto_suggest=False)
        except DisambiguationError as disambiguation:
            result = disambiguation.options
        except PageError:
            result = "no does not exist"
        print(result)
        query = input("Enter page title: ")


main()