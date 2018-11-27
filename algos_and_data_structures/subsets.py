def subsets(s):
    """ Returns all subsets of a list.
    Args:
        arr: a list
    Returns:
        All subsets of the list
    """
    # Base case
    if len(s) == 0:
        return [[]]
    # Divide and Conquer
    h, t = s[0], s[1:]
    ss_excl_h = subsets(t)
    ss_incl_h = [([h]+ss) for ss in ss_excl_h]
    return ss_incl_h + ss_excl_h

print(subsets('123'))
