# NAIVE SOLUTION
# our two sum function which will return
# all pairs in the list that sum up to S
def twoSum(arr, S):
  sums = []
  # check each element in array
  for i in range(0, len(arr)):
    # check each other element in the array
    for j in range(i+1, len(arr)):
      # determine if these two elements sum to S
      if (arr[i] + arr[j] == S):
        sums.append([arr[i], arr[j]])
  # return all pairs of integers that sum to S
  return sums


# TWO_SUM:  Attempts to find any two numbers in an array that sum up to a given number
# Input:    arr array, n numeric
# Output:   A list of lists containing pairs of numbers which sum to n
def two_sum(arr, n):
    # Append sums to out
    out = []
    # Dictionary for storage
    table = {}
    # Iterate through list
    for num in arr:
        # Store current number in dictionary
        table[num] = num
        # Check if there exists another number a in Dictionary
        # Such that a + num = n -> a = n - num
        if (n-num) in table.keys():
            # If so, append pair to out
            out.append([num,n-num])
    return out


def pass_test(func,arr,num):
    # Test for correctness
    # Get each pair
    pairs = func(arr,num)
    for s in pairs:
        # Sum the pair
        s = sum(s)
        # Check if sum equals num
        if s != num:
            print("Test Failed")
            return
    print("Test Passed")


def full_test(func, test_arr, test_num, test_dict):
    # Get func name
    func_name = func.__name__
    # Measure time function takes
    start= timer()
    ans = func(test_arr, test_num)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end-start
    # Test for correctness
    pass_test(func,test_arr,test_num)
    print("{}: {} seconds".format(func_name,test_dict[func_name]))
    print()


if __name__ == "__main__":
    from timeit import default_timer as timer
    import numpy as np
    test = {}
    test_num = np.random.randint(10)
    test_arr = np.random.randint(10,size=1000)
    full_test(twoSum, test_arr, test_num, test)
    full_test(two_sum, test_arr, test_num, test)
