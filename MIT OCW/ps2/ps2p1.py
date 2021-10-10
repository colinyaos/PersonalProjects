import string

def is_word_guessed(secret_word, letters_guessed):
    """Given string secret_word and list letters_guessed, find
    if the word has been guessed completely given the letters. 
    Returns boolean T/F. 
    Assume all letters are lowercase. """

    for character in secret_word:
        if not (character in letters_guessed):
            return False 
    return True

def get_guessed_word(secret_word, letters_guessed):
    """ Given string secret_word and list letters_guessed, 
    return string of letters, underscores, based on chars
    in letters_guessed that are in secret_word. 
    Use underscore+space to represent unknown letters. """

    return_string = ""

    for character in secret_word:
        if (character in letters_guessed):
            return_string += character + " "
        else:
            return_string += "_ "
    
    return return_string

def get_available_letters(letters_guessed):
    """Takes list letters_guessed. 
    Return string of lowercase English letters, 
    all which are not in letters_guessed. 
    Return all in alphabetical order. 
    Assume all chars in letters_guessed are lowercase."""

    all_letters = string.ascii_lowercase
    return_letters = ""

    for letter in all_letters:
        if not(letter in letters_guessed):
            return_letters += letter

    return return_letters

if __name__ == "__main__":

    ## tests go here

    target_word = "bananas"
    target_chars = ["a", "b", "c"]
    good_chars = ["a", "b", "n", "s"]
    more_chars = ["a", "b", "n", "s", "t", "d"]
    bad_chars = ["a", "x", "n"]

    print(get_available_letters(target_chars))
    print(get_available_letters(good_chars))
    print(get_available_letters(more_chars))
    print(get_available_letters(bad_chars))

    print(get_guessed_word(target_word, target_chars))
    print(get_guessed_word(target_word, good_chars))
    print(get_guessed_word(target_word, more_chars))
    print(get_guessed_word(target_word, bad_chars))