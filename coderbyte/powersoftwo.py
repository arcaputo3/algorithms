def PowersofTwo(num):
    while num > 1:
        num = num/2
    if num == 1.0:
        return 'true'
    else:
        return 'false'

print(PowersofTwo(16))
