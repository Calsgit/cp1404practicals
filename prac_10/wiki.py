import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    query = input("Enter page title: ")
    while query != "":
        result = ""
        try:
            print(wikipedia.summary(query, auto_suggest=False))
        except DisambiguationError as disambiguation:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(disambiguation.options)
        except PageError:
            print(f"Page id {query} does not match any pages. Try another id!")
        query = input("\nEnter page title: ")
    print("Thank you.")


main()