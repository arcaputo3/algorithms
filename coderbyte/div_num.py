def DivisionStringified(num1,num2):
    div = str(int(round(float(num1)/float(num2))))
    div_out = ''
    for i in range(len(div)-1):
        div_out += div[i]
        if (len(div)-(i+1)) % 3 == 0:
            div_out += ','
    div_out += div[-1]
    # code goes here
    return div_out
print(DivisionStringified(503394930,43))
