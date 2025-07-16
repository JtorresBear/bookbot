from stats import get_number_of_words 
from stats import character_count


# This function takes in a file path as a string
# then it prints the file after opening it. 

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


# get_book_text("./books/frankenstein.txt")

full_String = get_book_text("./books/frankenstein.txt")
 
letter_count = character_count(full_String)

print(letter_count)