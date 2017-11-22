"""We have an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
arrays A and B of n integers, a(0), a(1), ..., a(n-1) and b(0), b(1), ..., b(n-1)
respectively (0 <= a(i), b(i) <=  m).

The goal is to check whether there is a swap operation which can be performed
on these arrays in such a way that the sum of elements in array A equals
the sum of elements in array B after the swap. By swap operation we mean
picking one element from array A and one element from array B
and exchanging them.
"""

from helpers import print_out


@print_out
def slow_solution(A, B, m):
    """The simplest method is to swap every pair of elements and calculate the
    totals. Using that approach gives us O(n^3) time complexity. A better
    approach O(n^2) is to calculate the sums of elements at the beginning,
    and check only how the totals change during the swap operation.
    """
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    for i in range(n):
        for j in range(n):
            # Test swap
            change = B[j] - A[i]
            sum_a += change
            sum_b -= change
            if sum_a == sum_b:
                return True
            # Undo changes
            sum_a -= change
            sum_b += change
    return False


def counting(A, m):
    """Make an array of counters"""
    n = len(A)
    count = [0] * m
    for k in range(n):
        count[A[k]] += 1
    return count


@print_out
def fast_solution(A, B, m):
    """O(n + m): The best approach is to count the elements of array A
    and calculate the difference d between the sums of the elements of array A
    and B.

    For every element of array B, we assume that we will swap it with some
    element from array A. The difference d tells us the value from array A
    that we are interested in swapping, because only one value will cause
    the two totals to be equal. The occurrence of this value can be found
    in constant time from the array used for counting.
    """
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)

    d = sum_a - sum_b

    if d % 2 == 1:
        return False
    d //= 2

    count = counting(A, m)

    for i in range(n):
        if B[i] - d >= 0 and B[i] - d <= m and count[B[i] - d] > 0:
            return True

    return False


t1 = ([1, 4, 3, 1],
      [1, 6, 4, 2], 10)

t2 = ([1, 3, 3],
      [4, 4, 1], 10)

f1 = ([1, 3, 3, 1],
      [1, 6, 4, 2], 10)

f2 = ([1, 7, 3, 4],
      [1, 3, 4, 2], 10)

print('=== Slow:')
slow_solution(*t1)
slow_solution(*t2)
slow_solution(*f1)
slow_solution(*f2)
print('=== Fast:')
fast_solution(*t1)
fast_solution(*t2)  # TODO: false positive
fast_solution(*f1)
fast_solution(*f2)
