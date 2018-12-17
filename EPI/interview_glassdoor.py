import random

def remove_duplicates(arr):
    # Assume array is sorted
    return [arr[0]] + [arr[i] for i in range(1, len(arr)) if arr[i] != arr[i-1]]


#length = 10000
#lst1 = sorted([random.randint(0,10**5) for i in range(length)])
#print(remove_duplicates(lst1))


def remove_zeros(arr):
    for k in range(len(arr), 0, -1):
        if not arr[k-1]:
            arr.pop(k-1)
    return arr


#print(remove_zeros([1, 2, 4, 0, 5, 0, 1, 0, 0, 1, 7, 0, 8, 0, 2, 4, 5, 1, 2, 8, 0, 5, 6, 8] ))


def num_ones_int(n):
    count = 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        n //= 10
    return count

#print(num_ones_int(1231321))


def first_non_repeated_string(string):
    store = {}
    for v in string:
        if v in store:
            store[v] += 1
        else:
            store[v] = 1
    for key, val in store.items():
        if val == 1: return key
    return None

print(first_non_repeated_string("aazaabcccdddff"))


def div_wo_div(a, b):
    # represents a / b w/o div or mod operators
    div = 0
    while a >= b:
        a -= b
        div += 1
    return div, a

print(div_wo_div(9, 4))
