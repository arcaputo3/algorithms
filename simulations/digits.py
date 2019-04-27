
s = 0
for i in range(1234567, 7654322):
    if s == 2000:
        print(i)
    if i % 5 == 0:
        continue
    while i > 0:
        if i not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            continue
        i //= 10
    if i == 0:
        s += 1
