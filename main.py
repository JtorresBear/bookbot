import sys
from stats import get_number_of_words 
from stats import character_count
from stats import list_of_dictionaries_sorted_in_reverse


# This function takes in a file path as a string
# then it prints the file after opening it. 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


# get_book_text("./books/frankenstein.txt")

full_String = get_book_text(sys.argv[1])
count_dict = character_count(full_String)
num_of_words_in_text = get_number_of_words(sys.argv[1])
list_of_stuff = list_of_dictionaries_sorted_in_reverse(count_dict)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {num_of_words_in_text} total words")
print("--------- Character Count -------")
for item in list_of_stuff:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")


