"""Given a zero-indexed array A consisting of n integers:
a[0], a[1], ..., a[n−1]

Array represents a scenario in a grocery store, and contains only 0s and/or 1s:
- 0 represents the action of a new person joining the line in the grocery store,
- 1 the action of the person at the front of the queue being served and leaving
    the line.

The goal is to count the minimum number of people who should have been
in the line before the above scenario, so that the scenario is possible
(it is not possible to serve a person if the line is empty).

Solution O(n):
We should remember the size of the queue and carry out a simulation of people
arriving at and leaving the grocery store. If the size of the queue becomes
a negative number then that sets the lower limit for the number of people
who had to stand in the line previously. We should find the smallest negative
number to determine the size of the queue during the whole simulation.

The space complexity is O(1) because we don’t store people in the array,
but only remember the size of the queue.
"""


def grocery_store(A):
    n = len(A)
    size, result = 0, 0

    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size)

    return result
