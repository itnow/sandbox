"""Given array A consisting of N integers, return the reversed array"""

from helpers import print_out


@print_out
def reverse(arr):
    n = len(arr)
    for i in range(n // 2):
        k = n - i - 1
        arr[i], arr[k] = arr[k], arr[i]
    return arr


reverse([1, 2, 3, 4])
reverse([1, 2, 3, 4, 5])
