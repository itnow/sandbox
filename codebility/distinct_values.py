"""Given a zero-indexed array A consisting of n > 0 integers.

Return the number of unique values in array A.

Complexity of A.sort() is O(n * log n)

Solution O(n * log n):
Sort array A; similar values will then be next to each other.
Count the number of distinct pairs in adjacent cells.
"""

from helpers import print_out


@print_out
def distinct(A):
    n = len(A)
    if n < 1:
        return 0

    A.sort()
    result = 1
    for k in xrange(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result


distinct([0])
distinct([2, 1, 5, 2, 2])
