"""Count minimal number of jumps from position X to Y.

The frog is currently located at position X and wants to get to a position
greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform
to reach its target.
"""


def solution(X, Y, D):
    jumps = (Y - X) // D
    mod = (Y - X) % D
    if mod:
        return jumps + 1
    return jumps


print solution(10, 85, 30)
