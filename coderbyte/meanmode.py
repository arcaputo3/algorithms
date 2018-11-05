# MEANMODE:     Determines if the mean and mode of an array are equal
# Input:        numeric array arr
# Output:       1 if mean = mode, 0 o.w.
def MeanMode(arr):
    # Dictionary for getting mode
    store = {}
    # Sum for getting mean
    s = 0
    for elt in arr:
        # Store each element count
        if elt in store.keys():
            store[elt] += 1
        else:
            store[elt] = 1
        # Running sum
        s += elt
    # Get most frequent element
    mode = max(store, key=lambda k: store[k])
    # Get mean
    mean = s/len(arr)
    if mean == mode:
        return 1
    else:
        return 0
