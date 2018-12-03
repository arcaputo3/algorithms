# TWO WAYS TO DO PALINDROME

# First, simply join an ascending string followed by joining the descending string

# PALINDROME:   Prints palindromes up to size 2*n-1 starting with 1 (see example)
# INPUT:        int n
# OUTPUT:       palindromes up to n
def palindrome(n):
    for i in range(1,n+1):
        print(int(''.join(list(map(str,range(1,i+1)))) + ''.join(list(map(str,range(i-1,0,-1))))))
    return

# Finishes on 123454321
print(palindrome(5))


# Secondly, note that
# 1 = 1^2 = ((10^1-1)/9)^2
# 121 = 11^2 = ((10^2-1)/9)^2
# 12321 = 111^2 = ((10^3-1)/9)^2
# ...

# PALINDROME_:   Prints palindromes up to size 2*n-1 starting with 1 (see example)
# INPUT:        int n
# OUTPUT:       palindromes up to n
def palindrome_(n):
    for i in range(1,n+1):
        print(int((10**i-1)/9)**2)

# same output as palindrome(5)
print(palindrome_(5))
