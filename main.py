def main(): # Still need to take the lower case letters and break them up into a dictionary - Jan 5th
    book_location = "books/frankenstein.txt"
    words = book_text(book_location)
    word_count = word_counter(words)
    print(f"The book is {word_count} words")
    lower_case = small_letters(words)
    l_words = split_lower(lower_case)


def small_letters(words): # Convert the entire string to lower case
    l_case = words.lower()
    return l_case

def split_lower(lower_case): # Breaks up the lower case string into single words
    l_c_word = lower_case.split()
    return l_c_word

def word_counter(words): # Breaks the unedited string into single words then returns the word count
    word = words.split()
    return len(word)

def book_text(book_location): # Reads the file and puts it into a variable to be manipulated
    with open(book_location) as f:
        file_contents = f.read()
        return file_contents
main()