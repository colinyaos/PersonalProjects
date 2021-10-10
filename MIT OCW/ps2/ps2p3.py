from ps2p1 import *

def hangman_printer(letters_guessed, num_guesses):
    """Given list letters_guessed and int num_guesses, 
    print results of the hangman program. 
    Returns the string that was guessed. """

    available_string = get_available_letters(letters_guessed)
    
    if num_guesses > 1: 
        print("You have", num_guesses, "guesses left.")
    else:
        print("You have 1 guess left. ")
    print("Available letters: ", available_string)
    guessed_string = input("Please guess a letter: ")

    return guessed_string

def line_printer():
    """Prints a single line. That's it. Returns nothing. """
    print("--------------------\n")

def guess_returner(input_string, letters_guessed):
    """Returns True only if it's a valid guess. 
    Otherwise, returns False. 
    Guess is valid if 1 character, upper/lowercase English letter. 
    Invalid if in letters_guessed. """

    if len(input_string) == 0:
        print("You have to guess something. ")
        return False

    if len(input_string) > 1:
        print("Only one letter at a time, please. ")
        return False

    if not input_string.isalpha():
        print("That's not a letter of the alphabet. Try again. ")
        return False
    
    if input_string in letters_guessed:
        print("You already guessed the letter " + input_string + ". Try again. ")
        return False

    return True
    

def hangman(secret_word):
    """Takes string secret_word. Does the rest. 
    Prompts user for guesses, updates game state, etc. 
    3 warnings for invalid characters, 6 possible incorrect guesses. 
    Tells user when they are done, one way or another. """

    letters_guessed = []
    num_guesses = 6
    num_warnings = 3
    word_len = len(secret_word)
    is_complete = False

    print("Welcome to Hangman!")
    print("I am thinking of a word that is", word_len, "letters long. ")
    print("You have", num_warnings, "warnings left. ")
    line_printer()


    while(is_complete == False):

        temp_guess = hangman_printer(letters_guessed, num_guesses)
        
        if temp_guess == "*":
            print("Some possible words:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            if not guess_returner(temp_guess, letters_guessed): #This weeds out nonvalid guesses, like in l_g, but not wrong guesses. 
                num_warnings -= 1
                if num_warnings > 1:
                    print("You have", num_warnings, "warnings left. ")
                elif num_warnings == 1:
                    print("You have 1 warning left. ")
                elif num_warnings == 0:
                    print("You have no warnings left. ")
                else:
                    print("You have no warnings left, so you lose a guess instead. ")
                    num_guesses -= 1
            else:
                if temp_guess in secret_word:
                    print("That letter was in my word. ")
                else:
                    print("That letter was not in my word. ")
                    num_guesses -= 1
                letters_guessed.append(temp_guess)
        
            print(get_guessed_word(secret_word, letters_guessed))
        
        if num_guesses == 0:
            print("You're out of guesses. You lose. ")
            print("The word was: " + secret_word)
            break

        if is_word_guessed(secret_word, letters_guessed):
            is_complete = True
            break
        line_printer()
    
    if is_complete:
        print("Congratulations! You guessed my word. ")


## tests go here

# target_word = "bananas"
# target_chars = ["a", "b", "c"]
# good_chars = ["a", "b", "n", "s"]
# more_chars = ["a", "b", "n", "s", "t", "d"]
# bad_chars = ["a", "x", "n"]

# char_reader_bad_input = ["1", "q", "@", "word", "", "a"]

# for char in char_reader_bad_input:
#     print(guess_returner(char, target_chars))

# print(hangman_printer(target_word, target_chars, 2))
# hangman(target_word)