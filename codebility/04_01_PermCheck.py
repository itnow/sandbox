"""Check whether array A is a permutation.

A non-empty zero-indexed array A consisting of N integers is given.
A permutation is a sequence containing each element from 1 to N once, and
only once.

Assume that:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [1..1,000,000,000].
Complexity:
- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N).

Returns 1 if array A is a permutation and 0 if it is not.
"""

from helpers import print_out


@print_out
def solution(A):
    n = len(A)
    control_sum = n * (n + 1) // 2
    input_sum = sum(set(A))
    if control_sum == input_sum:
        return 1
    return 0


solution([4, 1, 3, 2])
solution([4, 1, 2])
solution([1])
solution([1, 4, 1])
