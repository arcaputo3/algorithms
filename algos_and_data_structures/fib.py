# FIB: 	Prints the nth Fibonacci number in O(n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 1st Fibonacci number is 1, 2nd Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def fib(n):
	if n <= 1:
		return 1
	a = 0
	b = 1
	for _ in range(n):
		a,b = b,a+b
	return a


# DYN_FIB: Prints the nth Fibonacci number in O(n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 1st Fibonacci number is 1, 2nd Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def dyn_fib(n):
    if n <= 2:
        return 1
    arr = [1,1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    return arr[-1]


# SLOW_FIB: 	Prints the nth Fibonacci number in O(2^n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 1st Fibonacci number is 1, 2nd Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def slow_fib(n):
	if n <= 2:
		return 1
	else:
		return slow_fib(n-1)+slow_fib(n-2)


# We can improve slow_fib by memorizing values at each call, i.e.
# MEMO_FIB: 	Prints the nth Fibonacci number in O(n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 1st Fibonacci number is 1, 2nd Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def memo_fib(n):
    memo = {}
    def memo_fib_(n,memo):
        if n in memo.keys():
            return memo[n]
        if n <= 2:
            result = 1
        else:
            result = memo_fib_(n-1, memo) + memo_fib_(n-2, memo)
        memo[n] = result
        return result
    return memo_fib_(n,{})


def full_test(func, test_num, test_dict):
    # Get sort_func name
    func_name = func.__name__
    # Measure time function takes
    start= timer()
    ans = func(test_num)
    end = timer()
    # Store time in test dictionary
    test_dict[func_name] = end-start
    # Print test results
    print("{}: {} seconds".format(func_name,test_dict[func_name]))
    print()


if __name__ == "__main__":
    from timeit import default_timer as timer
    num = 600
    test = {}
    full_test(fib, num, test)
    full_test(dyn_fib, num, test)
    full_test(memo_fib, num, test)
    test_view = [ (v,k) for k,v in test.items() ]
    test_view.sort() # natively sort tuples by first element
    print("From fastest to slowest:")
    for v,k in test_view:
        print("%s" % k)
