def fib(n):
	if n <= 0:
		return 0
	a = 0
	b = 1
	for _ in range(n):
		a,b = b,a+b
	return a

