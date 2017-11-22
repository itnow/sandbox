"""Find the missing element in a given permutation

A zero-indexed array A consisting of N different integers is given.
The array contains integers in the range [1..(N + 1)],
which means that exactly one element is missing.

Return the value of the missing element.
"""


def solution(A):
    print('<<<', A)

    # full length of array
    n = len(A) + 1
    # sum of full array
    control_sum = n * (n + 1) // 2
    # sum of input array
    input_sum = sum(A)

    # missed value is diff between sums
    return control_sum - input_sum


print(solution([2, 3, 1, 5]))
