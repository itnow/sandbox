"""Given a sequence a[0], a[1], ..., a[n-1].
Find the value of the leader of the sequence, such that 0 <= a[i] <= 10^9.
If there is no leader return -1.

The leader of sequence is the element whose value occurs more than n/2 times.

[6 8 4 6 8 6 6]
 0 1 2 3 4 5 6
"""

from helpers import print_out


@print_out
def slow_leader(A):
    """O(n^2)
    Count the occurrences of every element.
    """
    n = len(A)
    leader = -1
    for k in range(n):
        candidate = A[k]
        count = 0
        for i in range(n):
            if A[i] == candidate:
                count += 1
        if count > n // 2:
            leader = candidate
    return leader


@print_out
def fast_leader(A):
    """O(n * log n)
    If the sequence is presented in non-decreasing order, then identical values
    are adjacent to each other.

    The leader occurs in more than half (n/2) the total values in the sequence.
    It must occur at index n/2 - the central element.

    Sort sequence, pick middle element, count occurrences.
    """
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[n // 2]
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader


@print_out
def golden_leader(A):
    """O(n)
    If the sequence contains a leader, then after removing a pair of elements
    of different values, the remaining sequence still has the same leader.
    If we remove two dierent elements then only one of them could be the leader.

    The leader in the new sequence occurs more than (n/2)-1 = (n-2)/2 times.
    It is still the leader of the new sequence of n/2 elements.

    Let’s create an empty stack onto which we will be pushing consecutive elements.
    After each such operation we check whether the two elements at the top
    of the stack are dierent. If they are, we remove them from the stack.
    This is equivalent to removing a pair of dierent elements from the sequence.

    We don’t need to remember all the elements from the stack, because all
    the values below the top are always equal. It is sucient to remember only
    the values of elements and the size of the stack.

    After removing all pairs of dierent elements, we end up with a sequence
    containing all the same values. This value is not necessarily the leader;
    it is only a candidate for the leader.

    Finally, we should iterate through all the elements and count the occurrences
    of the candidate; if it is greater than n/2 then we have found the leader;
    otherwise the sequence does not contain a leader.
    """
    n = len(A)
    size = 0

    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1

    candidate = -1
    if size > 0:
        candidate = value

    leader = -1
    count = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate

    return leader


t1 = [6, 8, 4, 6, 8, 6, 6]
t2 = [7]
f1 = [2, 2, 1, 1, 2, 1]
f2 = [4, 5]

slow_leader(t1)
slow_leader(t2)
slow_leader(f1)
slow_leader(f2)

fast_leader(t1)
fast_leader(t2)
fast_leader(f1)
fast_leader(f2)

golden_leader(t1)
golden_leader(t2)
golden_leader(f1)
golden_leader(f2)
