"""Store the data by making an array of counters.

Each number may be counted in the array by using an index that corresponds
to the value of the given number.
"""

from helpers import print_out


@print_out
def counting(A, m):
    n = len(A)
    count = [0] * m

    for k in range(n):
        count[A[k]] += 1

    return count


counting([1, 3, 1, 5, 7], 10)
