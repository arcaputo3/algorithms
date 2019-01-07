# Birthday problem
# See https://math.stackexchange.com/questions/1804953/birthday-line-to-get-ticket-in-a-unique-setup for problem statement

# Plotting for use later
import matplotlib.pyplot as plt

def birthday_line_problem():
    # prob to be updated as probability that person at line index i does not share a birthday with anyone in front of them
    # First person in line is guaranteed not to share birthday with anyone in front
    probs = [1]
    # q to be updated as prob that no one else shares a birthday with anyone in front of us except for us (we stand at positon i)
    # We want to maximize this probability
    # First person in line cannot share a birthday with anyone in front
    q = [0]
    # By pigeonhole principle, after 366 people, two are guaranteed to share a birthday (ignoring leap year)
    for i in range(1, 366):
        # q = 0, 1/365 * 365/365, 2/365 * 365/365 * 364/365, ...
        # q[i] = i/365 * probs[i-1]
        q.append(probs[i-1]*i/365)
        # probs = 365/365, 365/365 * 364/365, 365/365 * 364/365 * 363/365, ...
        # probs[i] = probs[i-1]*(365-n)/365
        probs.append(probs[i-1]*(365-i)/365)
    # Get index of max value of q, add 1 to compensate for 0 indexing
    # Also return q for plotting
    # This is where we want to stand!
    return q.index(max(q)) + 1, q


if __name__ == "__main__":
    # Testing
    # Get best position and all probabilities
    best, q = birthday_line_problem()
    # Print best position
    print("The best position to stand in line is position {}".format(best))
    # Plot probabilities; notice how the distribution peaks at position 20
    plt.plot(q)
    plt.show()
