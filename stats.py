


def get_number_of_words(words):
    with open(words) as f:
        file_contents = f.read()

    collection_of_words = file_contents.split()
    print(f"{len(collection_of_words)} words found in the document")


def character_count( long_string):
    characters_dictionary = {}
    

    for character in long_string:
        sample_char = character.lower()
        if sample_char in characters_dictionary:
            characters_dictionary[sample_char] = characters_dictionary[sample_char] + 1
        else:
            characters_dictionary[sample_char] = 1

    return characters_dictionary


character_count("long string i think of EVERY LETTER IS BIG ON THIS SIDE")