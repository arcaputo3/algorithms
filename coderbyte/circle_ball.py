""" File for running circle ball passing game simulation. """

import numpy as np

def circle_ball_iter():
    """
    Runs a single simulation of the ball passing game:
    In a circle of ten people, starting at a certain position, pass the ball to
    the left or right, with equal probability.
    The game continues until only a single person has not been passed the ball,
    and that person wins. We seek to check the probability
    of any position to win given the starting position.
    """
    # Initialize circle
    circle = [0]*10
    # Ball starts in first position
    circle[0] = 1
    ball = 0
    # Continuation criterion: If sum == 9, all have been visited except one
    while sum(circle) != 9:
        # Randomize passing as uniform(0, 1)
        roll = np.random.rand()
        # Randomly pass to the right
        if roll >= 0.5:
            ball += 1
            # If we've exceded right indexing, bring ball to initial index
            if ball == 10:
                ball = 0
        # Randomly pass to the left
        else:
            ball -= 1
            # If we've exceded left indexing, bring ball to end
            if ball == -1:
                ball = 9
        # Check if we've visited before
        if circle[ball] == 0:
            # If this index hasn't seen the ball, increment count
            circle[ball] = 1
    # Return index that hasn't been indexed, corrected for 0 indexing
    # since we know ball starts at index 0
    return circle.index(0)-1


def circle_ball(iters=500000):
    """
    Runs circle_ball_iter iters number of times and averages
    over number of times we hit each index.

    Args:
        iters:  int number of iterations to run Monte Carlo algorithm.

    Returns:
        List containing probabilities of each index winning the game.
    """
    # Initialze list
    all_iters = [0]*9
    # Run algorithm iters number of times
    for _ in range(iters):
        # Get iteration run
        ball = circle_ball_iter()
        # Increment count
        all_iters[ball] += 1
    # Average over number of iters
    all_iters = list(map(lambda x: x/iters, all_iters))
    return all_iters

# To our suprise, each position seems to have equal probability of winning!
print(circle_ball())
