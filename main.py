def main(): #Add dictionary to sorted list
    book_location = "books/frankenstein.txt"
    words = book_text(book_location)
    word_count = word_counter(words)
    lower_case = small_letters(words)
    l_letters = letter_list(lower_case)
    dictionary_populate = dictionary(l_letters)
    sorted_dictionary = unsorted_to_sorted(dictionary_populate)

    print(f"The book is {word_count} long.")
    print()
    print("The following is the count of each letter in the book")
    for letter in sorted_dictionary:
        if not letter["let"].isalpha():
            continue
        print(f"There are {letter['num']} of the letter '{letter['let']}'")
    print()
    print("This concludes the count.")

def sort_on(dictionary_populate): # Required for the sort function to access dictionary entries
    return dictionary_populate["num"]

def unsorted_to_sorted(dictionary_populate):
    let_list = []
    for l in dictionary_populate:
        let_list.append({"let" : l, "num" : dictionary_populate[l]})
    let_list.sort(reverse = True, key = sort_on)
    return let_list

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