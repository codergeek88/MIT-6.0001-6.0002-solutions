# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def permutate_first_letter(original_list, first_letter, small_sequence_len):            
    permutations_list = []
        
    for word in original_list:
        for i in range(small_sequence_len + 1):
            new_permutation = word[0:i] + first_letter + word[i:small_sequence_len]
            permutations_list.append(new_permutation)
    return permutations_list

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
    
    sequence_len = len(sequence)        
    if sequence_len == 1:
        return list(sequence)
    else:
        first_letter = sequence[0]
        small_sequence_len = sequence_len - 1
        return permutate_first_letter((get_permutations(sequence[1:sequence_len])), first_letter, small_sequence_len)

if __name__ == '__main__':
    
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

