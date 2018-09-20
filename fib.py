# Input: Integer n
# Output: The nth Fibonacci number, where 0th Fibonacci number is 0, 1st Fibonacci number is 1.
def fib(n):
	if n <= 0:
		return 0
	a = 0
	b = 1
	for _ in range(n):
		a,b = b,a+b
	return a

