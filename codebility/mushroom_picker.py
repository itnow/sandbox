"""You are given a non-empty, zero-indexed array A
of n integers (1 <= n <= 100000)
a[0], a[1], ..., a[n-1] (0 <= a[i] <= 1000).

This array represents number of mushrooms growing on the consecutive spots
along a road. You are also given integers k and m (0 <= k, m < n).

A mushroom picker is at spot number k on the road and should perform m moves.
In one move she moves to an adjacent spot. She collects all the mushrooms
growing on spots she visits.

The goal is to calculate the maximum number
of mushrooms that the mushroom picker can collect in m moves.

For example, consider array A such that:
A  [2  3  7  5  1  3  9]
k   0  1  2  3 (4) 5  6
The mushroom picker starts at spot k = 4 and should perform m = 6 moves.

She might move to spots 3 > 2 > 3 > 4 > 5 > 6
and thereby collect mushrooms: 1 + 5 + 7 + 3 + 9 = 25

Or move 5 > 6 > 5 > 4 > 3 > 2
and collect same amount: 1 + 3 + 9 + 5 + 7 = 25

This is the maximal number of mushrooms she can collect.

Solution O(m^2):
The best strategy is to move in one direction optionally followed by some moves
in the opposite direction. In other words, the mushroom picker should not
change direction more than once. With this observation we can find the simplest
solution. Make the first p = 0, 1, 2, ..., m moves in one direction, then
the next m-p moves in the opposite direction. This is just a simple simulation
of the moves of the mushroom picker which requires O(m^2) time.

Solution O(n+m):
A better approach is to use prefix sums. If we make p moves in one direction,
we can calculate the maximal opposite location of the mushroom picker. The mushroom
picker collects all mushrooms between these extremes. We can calculate the total
number of collected mushrooms in constant time by using prefix sums.
"""

from helpers import print_out
from prefix_sums import prefix_sums, count_total


@print_out
def mushrooms(A, k, m):
    n = len(A)
    result = 0
    pref = prefix_sums(A)

    for p in xrange(min(m, k) + 1):
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    for p in xrange(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))

    return result


mushrooms([2, 3, 7, 5, 1, 3, 9], 4, 6)
