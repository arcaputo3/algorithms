def compare_max(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n % 2 == 1:
        arr.append(arr[-1])
    max_ = []
    while arr:
        a = arr.pop(0)
        b = arr.pop(0)
        max_.append(a if a >= b else b)
        a = None
        b = None
    if a and b:
        max_.append(a if a >= b else b)
    return compare_max(max_)

print(compare_max([20,2,3,3]))
