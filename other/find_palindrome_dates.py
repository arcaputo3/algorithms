import math

def create_palindrome(num):
    num_digits = math.floor(math.log10(num)) + 1
    mask = 10**(num_digits-1)
    beg = 1
    pal_num = 0
    while num:
        pal_num += (num // mask)*beg
        beg *= 10
        num %= mask
        mask //= 10
    return pal_num

def check_valid_mmdd(mmdd):
    mm  = mmdd // 100
    dd = mmdd % 100
    if mm in set((1, 3, 5, 7, 8, 10, 12)):
        return dd <= 31
    elif mm == 2:
        return dd <= 28
    else:
        return dd <= 30

def find_palindromic_dates():
    four_dig =  sum(check_valid_mmdd(create_palindrome(i)) for i in range(1000, 10000))
    three_dig = 9*sum(check_valid_mmdd(create_palindrome(i)) for i in range(1, 1000))
    return four_dig + three_dig

print(find_palindromic_dates())
