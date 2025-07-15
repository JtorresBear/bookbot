# This function takes in a file path as a string
# then it prints the file after opening it. 

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        print(file_contents)

def get_number_of_words(words):
    with open(words) as f:
        file_contents = f.read()

    collection_of_words = file_contents.split()
    print(f"{len(collection_of_words)} words found in the document")

# get_book_text("./books/frankenstein.txt")

get_number_of_words("./books/frankenstein.txt")
 