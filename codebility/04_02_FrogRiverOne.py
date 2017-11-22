"""Find the earliest time when a frog can jump to the other side of a river.

A small frog wants to get to the other side of a river. The frog is initially
located on one bank of the river (position 0) and wants to get to the opposite
bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given a zero-indexed array A consisting of N integers representing
the falling leaves. A[K] represents the position where one leaf falls
at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side
of the river. The frog can cross only when leaves appear at every position
across the river from 1 to X (that is, we want to find the earliest moment
when all the positions from 1 to X are covered by leaves).

You may assume that the speed of the current in the river is negligibly small,
i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:
[1, 3, 1, 4, 2, 3, 5, 4]
 0  1  2  3  4  5  6  7
In second 6, a leaf falls into position 5. This is the earliest time
when leaves appear in every position across the river.

Assume that:
- N and X are integers within the range [1..100,000];
- each element of array A is an integer within the range [1..X].
Complexity:
- expected worst-case time complexity is O(N);
- expected worst-case space complexity is O(X), beyond input storage.

Return the earliest time when the frog can jump to the other side of the river.
If the frog is never able to jump to the other side of the river,
the function should return -1.
"""

from helpers import print_out


@print_out
def solution(X, A):
    fall_time = len(A)
    leaves_pos = set()

    for t in range(fall_time):
        leaves_pos.add(A[t])
        if len(leaves_pos) == X:
            return t

    return -1


solution(1, [1])
solution(2, [1, 1])
solution(4, [1, 2, 3, 4])
solution(4, [1, 1, 2, 3])
solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
