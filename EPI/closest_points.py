""" Fast algorithms for detecting closest points in an array. """

import math
import random

def closest_points_1d(arr):
    """ Calculates the closest points in 1-d array.
    Args:
        arr:    int (float) list
    Returns:
        closest two points by euclidean distance.
    """
    arr = sorted(arr)
    min_dist = math.inf
    points = None
    for i, v in enumerate(arr[:-1]):
        current_dist = abs(v - arr[i+1])
        if current_dist <= min_dist:
            min_dist = current_dist
            points = (v, arr[i+1])
    return points


def dist(p, q):
    """ Computes distance between points p and q. """
    (x_1, y_1) = p
    (x_2, y_2) = q
    return math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)


def brute(arr):
    """ Gets closest points split between left and right division.
        BRUTE FORCE O(n^2)
    Args:
        p_x:    int (float) tuple list sorted by x-coordinate
        p_y:    int (float) tuple list sorted by y-coordinate
        delta:  minimum distance calculated in either left or right of plane
    Returns:
        p, q    such that p and q are closest points
                split by x_bar (center x value)
    """
    min_dist = dist(arr[0], arr[1])
    p = arr[0]
    q = arr[1]
    n = len(arr)
    if n== 2:
        return p, q
    for i in range(n - 1):
        for j in range(i + 1, n):
            if i != 0 and j != 1:
                current_dist = dist(arr[i], arr[j])
                if current_dist < min_dist:  # Update min_dist and points
                    min_dist = current_dist
                    p, q = arr[i], arr[j]
    return p, q


def closest_split_pair(p_x, p_y, delta):
    """ Gets closest points split between left and right division.
    Args:
        p_x:    int (float) tuple list sorted by x-coordinate
        p_y:    int (float) tuple list sorted by y-coordinate
        delta:  minimum distance calculated in either left or right of plane
    Returns:
        p, q    such that p and q are closest points
                split by x_bar (center x value)
    """
    n = len(p_x)
    x_bar = p_x[n//2-1][0] # Recall that left_x = p_x[:n//2], doesn't include n//2
    # Define range of possible x values in
    in_s_y = lambda l: x_bar - delta <= l <= x_bar + delta
    s_y = [p for p in p_y if in_s_y(p[0])]
    # Current best distance is delta
    best = delta
    # Initialize best pair
    best_pair = None
    for i in range(len(s_y) - 1):
        for j in range(i+1, min(i + 7, len(s_y))):
            p, q = s_y[i], s_y[j]
            if dist(p, q) < best:
                best = dist(p, q)
                best_pair = (p, q)
    return best_pair


def closest_pair(p_x, p_y):
    """ Recursive sub-routine for getting closest pair.
    Args:
        p_x:    int (float) tuple list sorted by x-coordinate
        p_y:    int (float) tuple list sorted by y-coordinate
    Returns:
        Closest points in p_x and p_y by euclidean distance.
    """
    # Get length
    n = len(p_x)
    if n <= 3:
        return brute(p_x)
    # Get left most points sorted by x
    left_x  = p_x[:n//2]
    # Get right most points sorted by x
    right_x = p_x[n//2:]
    # Get left most points sorted by y
    # Note that we need to iterate through p_y and keep only
    # x values that are less than or equal to the largest x-value in x_left
    left_y  = [p for p in p_y if p[0] <= left_x[-1][0]]
    # Get right most points sorted by y similarly
    right_y = [p for p in p_y if p[0] > left_x[-1][0]]
    # Recursive calls for left and right
    (p_1, q_1) = closest_pair(left_x, left_y)
    (p_2, q_2) = closest_pair(right_x, right_y)
    # Get min distance of previous pairs of points
    delta = min(dist(p_1, q_1), dist(p_2, q_2))
    # Third recursive call, necessary if closest points are in
    # left and right of plane respectively
    p_3_and_q_3 = closest_split_pair(p_x, p_y, delta)
    if p_3_and_q_3:
        return p_3_and_q_3
    return (p_1, q_1) if dist(p_1, q_1) == delta else (p_2, q_2)


def closest_points(arr):
    """ Calculates the closest 2-d points in an array of point tuples.
    Args:
        arr:    int (float) tuple list
    Returns:
        Closest two points by euclidean distance.
    """
    # Get X and Y points individually and sort
    p_x = sorted(arr, key=lambda x: x[0])
    p_y = sorted(arr, key=lambda x: x[1])
    # Define recursive sub-routine
    points = closest_pair(p_x, p_y)
    return points, dist(points[0], points[-1])


if __name__ == "__main__":
    def test_case(length: int = 100000):
        lst1 = [random.randint(-10**9, 10**9) for i in range(length)]
        lst2 = [random.randint(-10**9, 10**9) for i in range(length)]
        return lst1, lst2
    lst1, lst2 = test_case()
    print(closest_points(zip(lst1, lst2)))
