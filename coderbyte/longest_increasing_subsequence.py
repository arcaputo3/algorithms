def LongestIncreasingSequence(arr):
    # lis returns length of the longest increasing subsequence
    # in arr of size n
    n = len(arr)

    # Declare the list (array) for LIS and initialize LIS
    # values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range (1 , n):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    # return length of largest subsequence
    return max(lis)
# end of lis function


def EvenPairs(str):
    # Returns true if string contains a pair of even integers
    # Otherwise false
    # First order of business: split string where characters are not digits
    # Emptry string and list for storage
    num = ""
    num_list = []
    # Iterate through LongestIncreasingSequence
    for character in str:
        # Concat new numbers
        if character.isdigit():
            num += character
        # Else, create a break
        elif num != "":
            # Append number
            num_list.append(num)
            # Set number to empty string
            num = ""
    # Need to append last number if necessary
    if num != "":
        num_list.append(num)
    # Iterate through created num_list
    for n in num_list:
        # We can only have an even pair if last digit is even
        if int(n[-1]) % 2 == 0:
            # If any other digit is even, we have an even pair,
            # where we break two integers where first digit is even
            for i in n[:-1]:
                if int(i) % 2 == 0:
                    return True
    return False

print(EvenPairs("f09r27i8e67"))
