def ScaleBalancing(strArr):
    balance, weights = strArr[0], strArr[-1]
    balance = list(map(int, balance[1:-1].split(', ')))
    weights = list(map(int, weights[1:-1].split(', ')))
    poss_weights = dict(zip(weights, weights))
    weights_c = weights.copy()
    while len(weights_c ) > 1:
        current = weights_c.pop(0)
        for weight in weights_c :
            poss_weights[current + weight] = (current, weight) if current < weight else (weight, current)
    left, right = balance[0], balance[-1]
    if abs(left - right) in poss_weights.keys():
        val = poss_weights[abs(left - right)]
        return "{},{}".format(val[0],val[1]) if type(val) == type(()) else str(val)
    left_poss = [x + left for x in weights]
    right_poss = [x + right for x in weights]
    for i, val in enumerate(left_poss):
        if val in right_poss:
            w1 = weights[i]
            w2 = weights[right_poss.index(val)]
            if w1 > w2:
                w1, w2 = w2, w1
            return "{},{}".format(w1,w2)
    return "not possible"


print(ScaleBalancing(["[6, 2]", "[1, 10, 6, 5]"]))
