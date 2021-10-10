# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        copy_words = self.valid_words.copy()
        return copy_words

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_vowels = vowels_permutation.lower()
        upper_vowels = vowels_permutation.upper()
        shuffle_vowel_dict = {}
        for i in range(5):
            shuffle_vowel_dict[VOWELS_UPPER[i]] = upper_vowels[i]
            shuffle_vowel_dict[VOWELS_LOWER[i]] = lower_vowels[i]

        return shuffle_vowel_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        return_string = ""
        original_message = self.get_message_text()

        for char in original_message:
            if char in transpose_dict.keys():
                return_string += transpose_dict[char]
            else:
                return_string += char
        
        return return_string

        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        valid_words = self.get_valid_words()
        # generate list of possible vowel permutations using 4A method

        permut_list = get_permutations("aeiou")

        # setup dictionary of string:ints to receive and evaluate best permutation

        result_dictionary = {}
        for permut in permut_list:
            result_dictionary[permut] = 0

        # for each permutation:
        for permut in result_dictionary.keys():

        #   build a swap dictionary using method from SubMessage
            swap_dict = self.build_transpose_dict(permut)
        #   get encrypted message using getter
            encrypt_message = self.get_message_text()
        #   use dictionary to replace vowels with new vowels

            swapped_message = ""
            for char in encrypt_message:
                if char in swap_dict.keys():
                    swapped_message += swap_dict[char]
                else:
                    swapped_message += char

        #   use isWord method from above to iterate over words
            swap_list = swapped_message.split(" ")

        #   if word, increment corresponding int in list
            for word in swap_list:
                if is_word(valid_words, word):
                    result_dictionary[permut] += 1

        # print(result_dictionary)
        # if all values of intlist are zero, return original
        if sum(result_dictionary.values()) == 0:
            # print("Amazing!")
            return self.get_message_text
        # take index of largest int in intlist

        best_permut = ""
        best_score = 0
        for entry in result_dictionary.items():
            if entry[1] > best_score:
                best_permut = entry[0]
                best_score = entry[1]
        # pick out the corresponding permutation, use to re-decrypt message

        # print("The best permut is", best_permut, "with a score of", best_score)

            #   build a swap dictionary using method from SubMessage
        out_swap_dict = self.build_transpose_dict(best_permut)
            #   get encrypted message using getter
        out_encrypt_message = self.get_message_text()
            #   use dictionary to replace vowels with new vowels

        out_swapped_message = ""
        for char in out_encrypt_message:
            if char in out_swap_dict.keys():
                out_swapped_message += out_swap_dict[char]
            else:
                out_swapped_message += char

        # return undecrypted message
        return out_swapped_message



if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE

    text1 = "Seven sneaky snakes sell seashells down by the seashore. "
    text2 = "One hundred miles and running, because I have more than ninety-nine problems. "
    permut1 = "euioa"
    permut2 = "uioea"
    
    encrypter1 = SubMessage(text1)
    encrypter2 = SubMessage(text2)

    enc_dict1 = encrypter1.build_transpose_dict(permut1)
    enc_dict2 = encrypter1.build_transpose_dict(permut2)

    print("Original message:", encrypter1.get_message_text(), "Permutation:", permut1)
    print("Encryption:", encrypter1.apply_transpose(enc_dict1))
    enc_message = EncryptedSubMessage(encrypter1.apply_transpose(enc_dict1))
    print("Decrypted message:", enc_message.decrypt_message())

    print("Original message:", encrypter1.get_message_text(), "Permutation:", permut2)
    print("Encryption:", encrypter1.apply_transpose(enc_dict2))
    enc_message = EncryptedSubMessage(encrypter1.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message.decrypt_message())

    print("Original message:", encrypter2.get_message_text(), "Permutation:", permut1)
    print("Encryption:", encrypter2.apply_transpose(enc_dict1))
    enc_message = EncryptedSubMessage(encrypter2.apply_transpose(enc_dict1))
    print("Decrypted message:", enc_message.decrypt_message())

    print("Original message:", encrypter2.get_message_text(), "Permutation:", permut2)
    print("Encryption:", encrypter2.apply_transpose(enc_dict2))
    enc_message = EncryptedSubMessage(encrypter2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message.decrypt_message())

