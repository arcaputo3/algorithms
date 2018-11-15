def cum_sum(arr):
    sum = 0
    cum_sum = [0]
    for i in range(1,len(arr)):
        temp = arr[i-1] + sum
        cum_sum.append(temp)
        sum = temp
    return cum_sum

print(cum_sum([1,1,1,2,1,20]))
