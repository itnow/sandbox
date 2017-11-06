"""Find the smallest positive integer that does not occur in a given sequence.

An array A of N integers is given.
Return the smallest positive integer (greater than 0) that does not occur in A.

Given A = [1, 3, 6, 4, 1, 2]
    the function should return 5
Given A = [1, 2, 3]
    the function should return 4
Given A = [-1, -3]
    the function should return 1

Assume that:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [-1,000,000..1,000,000].
Complexity:
- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(N), beyond input storage
"""

from helpers import print_out


@print_out
def solution(A):
    A = list(set(A))
    A.sort()
    n = len(A)

    for i in xrange(0, n):
        if A[i] > 0 and A[i + 1] > 0:
            if A[i] + 1 != A[i + 1]:
                return A[i] + 1
    
    return A[i] + 1
    # return 1


solution([1, 3, 6, 4, 1, 2])
solution([1, 2, 3])
solution([-1, -3])
solution([-1, 1, 2, 3])
