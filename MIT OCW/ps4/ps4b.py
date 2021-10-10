# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
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
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        output_dictionary = {}
        ## let's use some ez conversions to unicode ints to automate this
        ## 65-90 are uppercase, 97-122 are lowercase

        for i in range(65, 91):
            # print("output of", i, "is", chr(i))

            out_char_num = ((i-65) + shift) % 26 + 65

            # print("output of", out_char_num, "is", chr(out_char_num))            

            output_dictionary[chr(i)] = chr(out_char_num)
        
        for i in range(97, 123):
            # print("output of", i, "is", chr(i))

            out_char_num = ((i-97) + shift) % 26 + 97

            # print("output of", out_char_num, "is", chr(out_char_num))            

            output_dictionary[chr(i)] = chr(out_char_num)
        
        return output_dictionary

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''

        shift_dic = self.build_shift_dict(shift)
        pre_text = self.get_message_text()
        post_text = ""
        
        # print(pre_text)
        for char in str(pre_text):
            if char.isalpha():
                post_text += shift_dic[char]
            else:
                post_text += char
        
        return post_text
        


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        copy_dict = self.encryption_dict.copy()
        return copy_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift %26

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # We split the self block into words, using split
        # Then, we iterate over keys, then words. 
        # If word is valid, add to value for key
        # Look for key with best value, then return that key with the decrypted text
        # 
        # Def list of values: len 26, a-z

        value_list = [0] * 26

        # def super: new list of lists: fill with internal message encrypted with each key - only the final strings
        super_list = []

        crypted_messages = []
        for i in range(26):
            crypted_messages.append(self.apply_shift(i))

        # print(len(super_list))
        # print(super_list[2])

        # for each string in super:
        for crypted_string in crypted_messages:
        #   create new list to hold word strings
            word_string_list = [""]
        #   for each character in super:
            for char in str(crypted_string):
        #       if alphabet:
                if char.isalpha():
                    word_string_list.append(word_string_list.pop() + char)
                    # print("added " + char)
        #           put into list
        #       if space: 
                if char == " ":
        #           increase list counter by 1
                    word_string_list.append("")
                # print(word_string_list)
            word_string_list = list(filter(None, word_string_list))
            super_list.append(word_string_list)
        
        # for i in range 26: 
        for i in range(26):
        #   for word in superlist(i):
            for word in super_list[i]:
        #       if word with key is valid:
                valid_words = self.get_valid_words()
                if word in valid_words:
        #           list value += 1
                    value_list[i] += 1
        # 
        # return list.index(max(value list)) 
        best_value = value_list.index(max(value_list))
        decrypted_message = self.apply_shift(best_value)

        return (best_value, decrypted_message)


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    story_string = get_story_string()
    
    decrypter = CiphertextMessage(story_string)

    print(story_string + "\n")
    print(decrypter.decrypt_message())


    ### Tests are all below here


    # test_text = "This is a message. "
    # new_test_text = "New message!"
    # test_shift = 4

    # # test = Message(test_text)
    # # print(test.get_message_text())
    # # print(len(test.get_valid_words()))

    # # print(test.apply_shift(3))

    # pt_test = PlaintextMessage(new_test_text, test_shift)
    # # print(pt_test.get_shift())
    # # print(pt_test.get_encryption_dict())
    # encrypt_message = pt_test.get_message_text_encrypted()
    # # print(pt_test.get_message_text())
    # # print(pt_test.change_shift(2))
    # # print(pt_test.get_message_text_encrypted())

    # ct_test = CiphertextMessage(encrypt_message)
    # print(ct_test.decrypt_message())

    # # Pathological Attack goes here

    # a = "4"
    # b = "b       , a"
    # c = "s11@$ asd"

    # a_test = PlaintextMessage(a, 3)
    # b_test = PlaintextMessage(b, 3)
    # c_test = PlaintextMessage(c, 3)

    # print(a_test.get_message_text_encrypted())
    # print(b_test.get_message_text_encrypted())
    # print(c_test.get_message_text_encrypted())
    



