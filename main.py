def main(): #Add dictionary to sorted list
    book_location = "books/frankenstein.txt"
    words = book_text(book_location)
    word_count = word_counter(words)
    print(f"The book is {word_count} words")
    lower_case = small_letters(words)
    l_letters = letter_list(lower_case)
    dictionary_populate = dictionary(l_letters)
    sorted_dictionary = unsorted_to_sorted(dictionary_populate)

def sort_on(dictionary_populate): # Required for the sort function to access dictionary entries
    return dictionary_populate["num"]

def unsorted_to_sorted(dictionary_populate):


def dictionary(l_letters): # Populates a dictionary of all letters and special characters
    letter_dictionary = {}
    for letter in l_letters:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
    return letter_dictionary

def letter_list(lower_case): # Breaks lower case letters into a list of all letters
    letter = list(lower_case)
    return letter

def small_letters(words): # Convert the entire string to lower case
    l_case = words.lower()
    return l_case

def word_counter(words): # Breaks the unedited string into single words then returns the word count
    word = words.split()
    return len(word)

def book_text(book_location): # Reads the file and puts it into a variable to be manipulated
    with open(book_location) as f:
        file_contents = f.read()
        return file_contents
main()