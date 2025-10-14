def main():
    sentence = input("Text: ").lower()
    word_to_count = count_words_in_string(sentence)
    display_dictionary_items(word_to_count)


def count_words_in_string(text):
    """Calculate the amount of times each word is used in a given string"""
    word_to_count = {}
    words = text.split(" ")
    for word in words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    return word_to_count

def display_dictionary_items(key_to_value):
    """Run through and print each dictionary key and its value"""
    for key in key_to_value:
        print(f"{key} : {key_to_value[key]}")

main()
