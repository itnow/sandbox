"""Find value that occurs in odd number of elements

A non-empty zero-indexed array A consisting of N integers is given. The array
contains an odd number of elements, and each element of the array can be paired
with another element that has the same value, except for one element
that is left unpaired.

Return the value of the unpaired element.
"""

from helpers import print_out


@print_out
def solution(A):
    d = dict()
    unpaired = None

    for el in A:
        d[el] = d.setdefault(el, 0) + 1

    print 'Elements counts:', d

    for k, v in d.items():
        if v % 2 > 0:
            unpaired = k

    return unpaired


solution([9, 3, 9, 5, 3, 9, 7, 9, 7])
