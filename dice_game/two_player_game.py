import numpy as np
import matplotlib.pyplot as plt

# TWO_PLAYER_30_SIDED_DIE_GAME
# See https://math.stackexchange.com/questions/377393/30-sided-die-2-player-game
# Player 1 picks an integer between 1-30. Player 2 then picks another integer between 1-30 knowing Player 1's integer.
# Player's cannot pick same number.
# The players then roll a 30 sided die
# Whoever's number is closer wins a value equal to the roll FROM the other player!
# We will solve this first using Monte Carlo and then with deterministic methods


# We define a single iteration of the game by considering all possible choices for Player 1 and Player 2
# In this instance, we assume that players are only attempting to maximize their gains and not attempting to minimize their opponents' gains.
# Note that Python is 0 indexed, but this is fine since the game using integers 1, 2, ..., 30 is equivalent to the game shifted left once, i.e. using integers 0,1,...,29
# We will simply add 1 to each dice roll after comparisons
def two_player_game_iter(n=30):
    # Rewards matrix for P1
    mat1 = np.zeros((n,n))
    # Rewards matrix for P2
    mat2 = np.zeros((n,n))
    # Roll 30-sided die
    roll = np.random.randint(n)
    # Iterate over all possible choices
    # i denotes P1, j denotes P2
    for i in range(n):
        for j in range(n):
            # If P1's choice is closer to roll
            # Add value of roll to P1's rewards matrix at (i,j) position
            if abs(roll - i) < abs(roll - j):
                mat1[i,j] += roll+1
            # Similar if P2's choice is closer to roll
            elif abs(roll - i) > abs(roll - j):
                mat2[i,j] += roll+1
    # Return each rewards matrix
    return mat1,mat2


# Next, we define a "full game" as a continous game with many iterations
# We will add each rewards matrix into a total matrix for each iteration
def full_game(iters,n=30):
    # Create empty total matrices
    total1 = np.zeros((n,n))
    total2 = np.zeros((n,n))
    # Simulate iters
    for _ in range(iters):
        # Get single iter
        mat1,mat2 = two_player_game_iter(n=n)
        # Add each payoff to totals
        total1 += mat1
        total2 += mat2
    return total1,total2


# Using full_game, we find the optimal strategy.
# To do this, we first consider Player 2's optimal strategy for each possible strategy of Player 1.
# Then, we maximize returns for Player 1 based on what she knows Player 2 will do.
def find_optimal_strategy(iters = 50000, n=30):
    # Get each total
    total1, total2 = full_game(iters=iters, n=n)
    # Since Player 2's choice depends on Player 1's choice, we will consider the net profit of Player 2
    # as the total winnings for Player 2 minues the total winnings for Player 1.
    # Get the best strategy of Player 2 for each choice of Player 1
    best_js = np.argmax(total2, axis=1)
    # Create empty array for each value
    best_strats = np.zeros((n,n))
    # Get each best strat
    for i in range(n):
        best_strats[i,best_js[i]] = total1[i,best_js[i]]
    # Find optimal strategy:
    optimal1,optimal2 = np.unravel_index(np.argmax(best_strats, axis=None), best_strats.shape)
    # Return expected payoff and optimal strategy (corrected for zero indexing)
    return total1[optimal1,optimal2]/iters, total2[optimal1,optimal2]/iters, (optimal1+1,optimal2+1)


# Finally, we will simulate this game showing the effect of paying off the other player
def simulate_optimal_game(strategy,iters=10000, n=30):
    # Unpack strategies
    (p1,p2) = strategy
    # Assume each player starts at 0
    player1 = [0]
    player2 = [0]
    # Iterate game
    # Start iterations at 1 to account for previous values
    for i in range(1,iters+1):
        roll = np.random.randint(n)+1
        # If p1 closer to roll, reward p1 and deduct p2 by value of roll
        if abs(roll - p1) < abs(roll - p2):
            player1.append(player1[i-1] + roll)
            player2.append(player2[i-1] - roll)
        # Similar for p2
        else:
            player1.append(player1[i-1] - roll)
            player2.append(player2[i-1] + roll)
    # Return lists of player earnings
    # Note that player1 = -player2
    return player1,player2


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
# CommonerG (https://math.stackexchange.com/users/74357/commonerg), 30-sided die, 2-player game, URL (version: 2013-05-01): https://math.stackexchange.com/q/377695

def easy_solve(n=30):
    # Use p1 and p2 to store expected payoffs per player
    p1 = []
    p2 = []
    # Get each possible dice roll in order
    l = list(range(1,n+1))
    x = (1/2)*(np.sqrt(2*n**2+2*n-3)-1)
    for i in range(n):
        # Let player 1 choose ith possible integer
        player1 = l[i]
        # Use aforementioned strategy
        if l[i] <= int(x):
            player2 = l[i]+1
            # Append expected value per player according to which integer is larger
            p1.append((1/n)*sum(l[:player1]))
            p2.append((1/n)*sum(l[player2-1:]))
        else:
            player2 = l[i]-1
            p2.append((1/n)*sum(l[:player2]))
            p1.append((1/n)*sum(l[player1-1:]))
    return p1,p2


# Now, we get best strategies using expected value
def get_best(p1,p2, n=30):
    # Get optimal EV for player1 given player1 knows player2's strategy
    bestp1 = max(p1)
    # Get index of EV, i.e. optimal strategy
    bestp1_ind = p1.index(bestp1)
    # p2 already is using optimal strategy for each index, just need value
    bestp2 = p2[bestp1_ind]
    # Get correct true index for player1
    x = (1/2)*(np.sqrt(2*n**2+2*n-3)-1)
    bestp2_ind = bestp1_ind + 1 if bestp1_ind+1<=int(x) else bestp1_ind - 1
    # Return tuples (strategy_i, expected_payoff_i) for i in {1,2}
    return (bestp1_ind+1, bestp1), (bestp2_ind+1, bestp2)


if __name__ == "__main__":
    # Choose n-sided die
    n=30
    # Simulate each possible strategy
    # Get each players' payoff for each strategy as well as the optimal strategy (strat)
    EV1,EV2, strat = find_optimal_strategy(iters=10000,n=n)
    p1,p2 = strat
    print("Monte Carlo Results:")
    print("Optimal Strategy and Expected Payoff for Player 1: {}".format((p1,EV1)))
    print("Optimal Strategy and Expected Payoff for Player 2: {}".format((p2,EV2)))
    print()
    # Run simulation using optimal strategy
    player1,player2 = simulate_optimal_game(strat, n=n)
    # Plot outcomes: Notice that player 1 has slight advantage
    plt.plot(player1)
    plt.plot(player2)
    plt.legend(['Player 1','Player 2'], loc = 'upper left')
    plt.title('Simulation of Dice Game with Payoff Refactoring')
    plt.xlabel('Number of Iterations')
    plt.ylabel('Net Payoff')
    plt.show()
    # Now use easy_solve
    p1,p2=easy_solve(n=n)
    p1_,p2_ = get_best(p1, p2, n=n)
    print("Deterministic Results:")
    print("Optimal Strategy and Expected Payoff for Player 1: {}".format(p1_))
    print("Optimal Strategy and Expected Payoff for Player 2: {}".format(p2_))
    plt.plot(p1)
    plt.plot(p2)
    plt.legend(['Player 1','Player 2'], loc = 'upper left')
    plt.title('Expected Payoff per Player')
    plt.xlabel('Choice of Player 1')
    plt.ylabel('Expected Payoff')
    plt.show()
