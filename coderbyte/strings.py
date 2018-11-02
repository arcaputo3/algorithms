# Code for string based functions

# LETTERCHANGES:
# Input:    string str
# Output:   string str with all alphabetical characters shifted right 1 (i.e. a -> b, b -> c,... z -> a)
#           and all vowels capitalized
def LetterChanges(str):
    # Get vowels
    vowels = 'aeiou'
    new = ''
    # Iterate through each char in string
    for c in str:
        # Only change alphabetical characters
        if c.isalpha():
            # Lower for comparison
            c = c.lower()
            # Case for z
            if c == 'z':
                c = 'A'
            # Shift right using ord and chr
            else:
                c = chr(ord(c)+1)
                # Capitalize if we get vowel
                if c in vowels:
                    c = c.upper()
        # Append to output
        new += c
    return new

# keep this function call here
print(LetterChanges('abcsdjasdfgirtrij'))
