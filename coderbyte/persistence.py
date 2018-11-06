def AdditivePersistence(num):
    count = 0
    while num > 9:
        num = sum(map(int,str(num)))
        count += 1
    return count


def MultiplicativePersistence(num):
    count = 0
    while num > 9:
        num = map(int,str(num))
        prod = 1
        for x in num:
            prod *= x
        num = prod 
        count += 1
    return count

print(AdditivePersistence(1234))
print(MultiplicativePersistence(1234))
