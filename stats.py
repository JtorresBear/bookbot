


def get_number_of_words(words):
    with open(words) as f:
        file_contents = f.read()

    collection_of_words = file_contents.split()
    #print(f"{len(collection_of_words)} words found in the document")
    return len(collection_of_words)

# returns a dictionary with characters for keys 
# and counts for how many times the character appears in the text

def character_count( long_string):
    characters_dictionary = {}
    

    for character in long_string:
        sample_char = character.lower()
        if sample_char in characters_dictionary:
            characters_dictionary[sample_char] = characters_dictionary[sample_char] + 1
        else:
            characters_dictionary[sample_char] = 1

    return characters_dictionary

def sort_on(items):
    return items["num"]

# takes a dictionary, and makes a list of dictionaries and then sorts them. 
# it also prints in a way that looks nice
def list_of_dictionaries_sorted_in_reverse( some_dict ):
    dictionary_items = some_dict.items()
    char_and_number = []

    for item in dictionary_items:
        char, num = item
        char_and_number.append({"char":char, "num": num})
    
    char_and_number.sort(reverse=True,key=sort_on)
    return char_and_number


random = {
    "a": 4,
    "b": 5,
    "c": 23,
    "d": 1,
    "e": 400
}
