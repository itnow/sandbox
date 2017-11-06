"""Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

A non-empty zero-indexed array A consisting of N integers is given.
Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty
parts: A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N - 1].

The difference between the two parts is the value of:
|(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|

In other words, it is the absolute difference between the sum of the first
part and the sum of the second part.

Return the minimal difference that can be achieved.
"""

from helpers import print_out


@print_out
def solution(A):
    n = len(A)
    mindiff = None
    p1_sum = sum(A)
    p2_sum = 0

    for p in range(0, n - 1):
        el = A.pop()
        p1_sum -= el
        p2_sum += el
        diff = abs(p1_sum - p2_sum)

        if mindiff is None:
            mindiff = diff
        if diff < mindiff:
            mindiff = diff

    return mindiff


solution([3, 1, 2, 4, 3])
solution([-1000, 1000])
