def DashInsert(str):
    out = ''
    for i in range(len(str)-1):
        if (int(str[i]) % 2 == 1) and (int(str[i+1]) % 2 == 1):
            out += str[i] + '-'
        else:
            out += str[i]
    out += str[-1]
    # code goes here
    return out
