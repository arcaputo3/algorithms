# FIB: 	Prints the nth Fibonacci number in O(n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 0th Fibonacci number is 1, 1st Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def fib(n):
	if n <= 0:
		return 1
	a = 0
	b = 1
	for _ in range(n):
		a,b = b,a+b
	return a


# SLOW_FIB: 	Prints the nth Fibonacci number in O(2^n) time
# Input: 	Integer n
# Output:	The nth Fibonacci number, where 0th Fibonacci number is 1, 1st Fibonacci number is 1,
#			and the nth Fibonacci number is the (n-2)th Fib. number plus the (n-1)th Fib. number (n >= 0)
def slow_fib(n):
	if n <= 1:
		return 1
	else:
		return slow_fib(n-1)+slow_fib(n-2)
