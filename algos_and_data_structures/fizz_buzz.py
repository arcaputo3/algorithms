def fizz_buzz(nums):
    """
    Classic FizzBuzz: multiples of 3: Fizz, multiples of 5: Buzz
    """
    fizz_buzz = {3: "Fizz", 5: "Buzz"}
    out = []
    for n in nums:
        ans = ""
        for i, v in fizz_buzz.items():
            if n % i == 0:
                ans += v
        out.append(ans if ans else n)
    return out


def decomp(num):
    while num:
        yield num % 10
        num //= 10


def num_dig(r, n):
    """ Returns count of numbers from 1 to n which contain digit r. """
    return sum(str(r) in str(i) for i in range(1, n+1))




print(max_weight_IS([10, 20, 5, 6]))
print(num_dig(6, 600000))
