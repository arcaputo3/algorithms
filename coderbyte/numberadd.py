def NumberAddition(str):
    hold = ''
    total = 0
    for n in str:
        try:
            val = int(n)
            hold += n
        except ValueError:
            if hold != '':
                total += int(hold)
                hold = ''
    if hold != '':
        total += int(hold)
    # code goes here
    return total

print(NumberAddition('1 2 3 laksdjflasdkj 44'))
