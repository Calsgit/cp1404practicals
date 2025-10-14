def main():
    sentence = input("Text: ").lower()
    word_to_count = count_words_in_string(sentence)
    display_dictionary_items(word_to_count)


def count_words_in_string(text):
    """Calculate the amount of times each word is used in a given string"""
    word_to_count = {}
    words = sorted(text.split(" "))
    for word in words:
        try:
            word_to_count[word] += 1
        except KeyError:
            word_to_count[word] = 1
    return word_to_count

def display_dictionary_items(key_to_value):
    """Run through and print each dictionary key and its value"""
    max_length = max(len(key) for key in key_to_value)
    for key in key_to_value:
        print(f"{key:{max_length}} : {key_to_value[key]}")

main()
