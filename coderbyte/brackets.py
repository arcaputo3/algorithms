# BRACKETS: Given an int n, return every possible string of balanced brackets
#           such that we have n left brackets and n right brackets
# Input:    int n
# Output:   list containing all possible balanced brackets of size 2n
def brackets(n):
    arr = []
    # Subroutine to get brackets
    def brackets_(left, right, string):
        # Base case: we are done
        if left == 0 and right == 0:
            arr.append(string)
        # Recursive step: append left bracket and need a right bracket to balance
        if left > 0:
            brackets_(left-1, right+1, string+'(')
        # Recursive step: append right bracket (only happens after left bracket)
        if right > 0:
            brackets_(left, right-1, string+')')
    # Sub routine call
    brackets_(n,0,'')
    return arr

# In the case left = 2:

# Begin:
# left = 2, right = 0
# left > 0:
#   now have string = '('
#   left = 1, right = 1

# first recursion:
# left > 0:
#   first recursion has string = '(('
#   left = 0, right = 2
# right > 0:
#   first recursion has string = '(()'
#   left = 0, right = 1
# right > 0:
#   first recursion has string = '(())'
# left == 0, right == 0
# arr = ['(())']

# second recursion
# right > 0:
#   second recursion has string '()'
#   left = 1, right = 0
# left > 0:
#   second recusion has string '()('
#   left = 0, right = 1
# right > 0:
#   second recusion has string '()()'
# left == 0, right == 0
# arr = ['(())','()()']

# Some examples
print(brackets(2))
print(brackets(3))
print(brackets(4))
print(brackets(5))
