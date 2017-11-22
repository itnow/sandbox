"""Calculate sums of elements in given slice (contiguous segments of array).
Its main idea uses prefix sums which are defined as the consecutive totals
of the first 0, 1, 2, ..., n elements of an array.

Each consecutive value can be calculated in a constant time O(n).


Similarly, we can calculate suffix sums, which are the totals of the k last values.
Using prefix (or suffix) sums allows us to calculate the total of any slice
of the array very quickly.

For example, assume that you are asked about the totals of m slices [x..y]
such that 0 <= x <= y < n, where the total is the sum
a[x] + a[x+1] + ... + a[y-1] + a[y]

The simplest approach is to iterate through the whole array for each result
separately; however, that requires O(n*m) time. The better approach is
to use prefix sums. If we calculate the prefix sums then we can answer
each question directly in constant time.

To calculate the total of slice let's subtract p[x] from the value p[y+1].
It's O(1) time. Using this approach, the total time complexity is O(n + m).
"""

from helpers import print_out


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P, x, y):
    return P[y + 1] - P[x]


@print_out
def total_of_slice(A, x, y):
    P = prefix_sums(A)
    total = count_total(P, x, y)
    return total


if __name__ == '__main__':
    total_of_slice([1, 2, 3, 4, 5], 1, 3)
    total_of_slice([4, 3, 5, 2, 1], 1, 3)
