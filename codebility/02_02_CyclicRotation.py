"""Rotate an array to the right by a given number

A zero-indexed array A consisting of N integers is given. Rotation of the array
means that each element is shifted right by one index, and the last element
of the array is also moved to the first place.

Return the array A rotated K times.
"""


def solution(a, k):
    print '<<<', a, k
    if k > 0:
        a = a[-1:] + a[:-1]
        return solution(a, k - 1)
    return a


print solution([1, 2, 3, 4, 5], 2)
