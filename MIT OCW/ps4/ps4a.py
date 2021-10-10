# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Note: be wary of duplicates.
    # 
    # Desired strategy: Iterate over letters within original list
    # Repeat using recursion over each substring, returning list each time, to find all
    # Remember to eliminate dupes when done
    # 
    # declare master list

    master_list = []

    # for letter in sequence:
    for i in range(len(sequence)):
    
    #   store letter - this is the first in sequence
        first_char = sequence[i]
    #   Generate list of substrings: if no sub, return bare letter
        if len(sequence) == 1:
            return [sequence,]
        else:
            # print("first char is", first_char, "index is", i)
            # print("rest of substring is", sequence[:i] + sequence[i+1:])
            list_subs = get_permutations(sequence[:i] + sequence[i+1:])
            # print(list_subs)
        
        for element in list_subs:
            # print(first_char, element)
            master_list.append(first_char + element) 
    #       
    #   put letter in front of all substrings

    # print(master_list)
    # 
    # Eliminate dupes

    return list(set(master_list))
    #
    # Return list of strings






if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    z = "ab"
    a = "abc"
    b = "abcd"
    c = "abcde"
    d = "aaaaa"
    e = "aabbc"
    f = "aaabb"

    print(get_permutations(b))
    print(len(get_permutations(c)))
    
    print(len(get_permutations(d)))
    print(len(get_permutations(e)))
    print(get_permutations(f))


