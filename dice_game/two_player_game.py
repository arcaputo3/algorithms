""" Two Player Dice Game: Monte Carlo and Deterministic Solutions. """

import numpy as np
import matplotlib.pyplot as plt


# TWO_PLAYER_30_SIDED_DIE_GAME
# See https://math.stackexchange.com/questions/377393/30-sided-die-2-player-game
# Player 1 picks an integer between 1-30. Player 2 then picks another integer
# between 1-30 knowing Player 1's integer.
# Player's cannot pick same number.
# The players then roll a 30 sided die
# Whoever's number is closer wins a value equal to the roll FROM the other player!
# We will solve this first using Monte Carlo and then with deterministic methods


# We define a single iteration of the game by considering all possible choices
# for Player 1 and Player 2
# In this instance, we assume that players are only attempting to maximize
# their gains and not attempting to minimize their opponents' gains.
# Note that Python is 0 indexed, but this is fine since the game using integers
# 1, 2, ..., 30 is equivalent to the game shifted left once,
# i.e. using integers 0,1,...,29.
# We will simply add 1 to each dice roll after comparisons
def two_player_game_iter(n=30):
    """ Takes as input an n-sided die and produces a single iteration
    of the game.
    Args:
        n: int representing number of sides on die.
    Returns:
        Two matrices representing an iteration of each possible strategy
        for each player.
    """
    # Rewards matrix for P1
    mat_1 = np.zeros((n, n))
    # Rewards matrix for P2
    mat_2 = np.zeros((n, n))
    # Roll 30-sided die
    roll = np.random.randint(n)
    # Iterate over all possible choices
    # i denotes P1, j denotes P2
    for i in range(n):
        for j in range(n):
            # If P1's choice is closer to roll
            # Add value of roll to P1's rewards matrix at (i,j) position
            if abs(roll - i) < abs(roll - j):
                mat_1[i, j] += roll + 1
            # Similar if P2's choice is closer to roll
            elif abs(roll - i) > abs(roll - j):
                mat_2[i, j] += roll + 1
    # Return each rewards matrix
    return mat_1, mat_2


# Next, we define a "full game" as a continous game with many iterations
# We will add each rewards matrix into a total matrix for each iteration
def full_game(iters, n=30):
    """ Runs many iterations of the two_player_game_iter, totalling results.
    Args:
        iters:  int number of iterations.
        n:      int representing number of sides on die.
    Returns:
        Total summed simulations for player_1 and player_2.
    """
    # Create empty total matrices
    total_1 = np.zeros((n, n))
    total_2 = np.zeros((n, n))
    # Simulate iters
    for _ in range(iters):
        # Get single iter
        mat_1, mat_2 = two_player_game_iter(n=n)
        # Add each payoff to totals
        total_1 += mat_1
        total_2 += mat_2
    return total_1, total_2


# Using full_game, we find the optimal strategy.
# To do this, we first consider Player 2's
# optimal strategy for each possible strategy of Player 1.
# Then, we maximize returns for Player 1 based on what she knows Player 2 will do.
def find_optimal_strategy(iters=50000, n=30):
    """ Finds the optimal strategy for both players by backsolving for player_2
    and then forward solving for player_1.
    Args:
        iters:  int number of iterations.
        n:      int representing number of sides on die.
    Returns:
        Expected payoffs for player_1 and player_2, respectively, as well as a
        tuple representing the optimal strategy for player_1 and player_2, respectively.
    """
    # Get each total
    total_1, total_2 = full_game(iters=iters, n=n)
    # Since Player 2's choice depends on Player 1's choice, we will consider the net profit of Player 2
    # as the total winnings for Player 2 minues the total winnings for Player 1.
    # Get the best strategy of Player 2 for each choice of Player 1
    best_js = np.argmax(total_2, axis=1)
    # Create empty array for each value
    best_strats = np.zeros((n, n))
    # Get each best strat
    for i in range(n):
        best_strats[i, best_js[i]] = total_1[i, best_js[i]]
    # Find optimal strategy:
    optimal_1, optimal_2 = np.unravel_index(np.argmax(best_strats, axis=None), \
                                         best_strats.shape)
    # Return expected payoff and optimal strategy (corrected for zero indexing)
    return  total_1[optimal_1, optimal_2]/iters, \
            total_2[optimal_1, optimal_2]/iters, \
            (optimal_1 + 1, optimal_2 + 1)


# Finally, we will simulate this game showing the effect of paying off the other player
def simulate_optimal_game(strategy, iters=10000, n=30):
    """ Simulates many iterations of the game using the optimal Monte Carlo
    strategy. In this simulation, each player pays the other when they lose.
    Args:
        strategy:   int tuple representing optimal strategy.
        iters:      int number of iterations to run game.
        n:          int representing number of sides on die.
    Returns:
        Two lists containing earnings for each player at each time step.
    """
    # Unpack strategies
    (p_1, p_2) = strategy
    # Assume each player starts at 0
    player_1 = [0]
    player_2 = [0]
    # Iterate game
    # Start iterations at 1 to account for previous values
    for i in range(1, iters + 1):
        roll = np.random.randint(n) + 1
        # If p1 closer to roll, reward p1 and deduct p2 by value of roll
        if abs(roll - p_1) < abs(roll - p_2):
            player_1.append(player_1[i-1] + roll)
            player_2.append(player_2[i-1] - roll)
        # Similar for p2
        else:
            player_1.append(player_1[i-1] - roll)
            player_2.append(player_2[i-1] + roll)
    # Return lists of player earnings
    # Note that player1 = -player2
    return player_1, player_2


# Note that a MUCH simpler way to solve this is using sums
# Credit to CommonerG from math.stackexchange.com
# Intuitively, we know that player2 should choose a value as close to player1 as possible, either + or - 1.
# This will maximize the likelihood of winning given the choice of player1.
# Let x be the value of player1's integer such that player2's EV is higher if player2 chooses a value larger than player1
# We solve for (1/30)(sum from i=x+1 to i=30) >= (1/30)(sum from j=1 to j=x-1)
# Set equal for optimal value
# This comes out to 464-x-x^2 >= 0. Solving for x yields x <= ~21.56.
# We can generalize such that for any n-sided die,
    #   x = (1/2)*(sqrt(2n^2+2n-3)-1)
# Therefore, if player1 chooses 21 or lower, player2 should choose x+1. Otherwise, player2 should choose x-1.
# Backsolving for each possible choice of x knowing what player 2 will choose, we land at x=22 and player2 chooses 21.

# CITATION
# CommonerG (https://math.stackexchange.com/users/74357/commonerg),
# 30-sided die, 2-player game,
# URL (version: 2013-05-01): https://math.stackexchange.com/q/377695

def easy_solve(n=30):
    """ Solves game deterministically (forward solve).
    Args:
        n:  int representing number of sides on die.
    Returns:
        Lists of optimal strategy for player1 and player2, respectively.
    """
    # Use p1 and p2 to store expected payoffs per player
    p_1 = []
    p_2 = []
    # Get each possible dice roll in order
    arr = list(range(1, n + 1))
    x = (1/2)*(np.sqrt(2*n**2 + 2*n - 3) - 1)
    for i in range(n):
        # Let player 1 choose ith possible integer
        player_1 = arr[i]
        # Use aforementioned strategy
        if arr[i] <= int(x):
            player_2 = arr[i] + 1
            # Append expected value per player according to which integer is larger
            p_1.append((1/n)*sum(arr[:player_1]))
            p_2.append((1/n)*sum(arr[player_2-1:]))
        else:
            player_2 = arr[i] - 1
            p_2.append((1/n)*sum(arr[:player_2]))
            p_1.append((1/n)*sum(arr[player_1-1:]))
    return p_1, p_2


# Now, we get best strategies using expected value
def get_best(p_1, p_2, n=30):
    """ Solves game deterministically (backsolve).
    Args:
        n:  int representing number of sides on die.
    Returns:
        Optimal strategy and payoff tuples for player1 and player2, respectively.
    """
    # Get optimal EV for player1 given player1 knows player2's strategy
    best_p_1 = max(p_1)
    # Get index of EV, i.e. optimal strategy
    best_p_1_ind = p_1.index(best_p_1)
    # p2 already is using optimal strategy for each index, just need value
    best_p_2 = p_2[best_p_1_ind]
    # Get correct true index for player1
    x = (1/2)*(np.sqrt(2*n**2 + 2*n - 3) - 1)
    best_p_2_ind = best_p_1_ind + 1 if best_p_1_ind + 1 <= int(x) \
                                    else best_p_1_ind - 1
    # Return tuples (strategy_i, expected_payoff_i) for i in {1,2}
    return (best_p_1_ind + 1, best_p_1), (best_p_2_ind + 1, best_p_2)


if __name__ == "__main__":
    # Choose n-sided die
    N = 6
    # Simulate each possible strategy
    # Get each players' payoff for each strategy as well as the optimal strategy (strat)
    EV_1, EV_2, STRAT = find_optimal_strategy(iters=10000, n=N)
    P_1, P_2 = STRAT
    print("Monte Carlo Results:")
    print("Optimal Strategy and Expected Payoff for Player 1: {}".format((P_1, EV_1)))
    print("Optimal Strategy and Expected Payoff for Player 2: {}".format((P_2, EV_2)))
    print()
    # Run simulation using optimal strategy
    PLAYER_1, PLAYER_2 = simulate_optimal_game(STRAT, n=N)
    # Plot outcomes: Notice that player 1 has slight advantage
    plt.plot(PLAYER_1)
    plt.plot(PLAYER_2)
    plt.legend(['Player 1', 'Player 2'], loc='upper left')
    plt.title('Simulation of Dice Game with Payoff Refactoring')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Net Payoff')
    plt.show()
    # Now use easy_solve
    P_1_ALL, P_2_ALL = easy_solve(n=N)
    P_1_BEST, P_2_BEST = get_best(P_1_ALL, P_2_ALL, n=N)
    print("Deterministic Results:")
    print("Optimal Strategy and Expected Payoff for Player 1: {}".format(P_1_BEST))
    print("Optimal Strategy and Expected Payoff for Player 2: {}".format(P_2_BEST))
    plt.plot(P_1_ALL)
    plt.plot(P_2_ALL)
    plt.legend(['Player 1', 'Player 2'], loc='upper left')
    plt.title('Expected Payoff per Player')
    plt.xlabel('Choice of Player 1')
    plt.ylabel('Expected Payoff')
    plt.show()
