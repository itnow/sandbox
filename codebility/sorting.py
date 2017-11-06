from helpers import print_out


@print_out
def selection_sort(A):
    """O(n^2)
    Find the minimal element and swap it with the first element of an array.
    Next, sort the rest of the array, without the first element, in the same way.

    Notice that after k iterations the first k elements will be sorted
    in the right order (this type of a property is called the loop invariant).
    """
    n = len(A)
    for k in xrange(n):
        minimal = k
        for j in xrange((k + 1), n):
            if A[j] < A[minimal]:
                minimal = j
        if k != minimal:
            A[k], A[minimal] = A[minimal], A[k]
    return A


@print_out
def counting_sort(A, k):
    """O(n+k)
    First, count the elements in the array of counters. Next, just iterate
    through the array of counters and build sorted data from counters.

    Notice that we have to know the range (k) of the sorted values.
    If all the elements are in the set {0, 1, ..., k}, then the array used
    for counting should be of size k+1.

    Need an additional memory O(k) to count all the elements.
    """
    n = len(A)
    count = [0] * (k + 1)

    for i in xrange(n):
        count[A[i]] += 1
    idx = 0
    for el in xrange(k + 1):
        for _ in xrange(count[el]):
            A[idx] = el
            idx += 1
    return A


"""Divide the unsorted array into two halves, sort each half separately and then just
merge them. After the split, each part is halved again.
We repeat this algorithm until we end up with individual elements, which are sorted by
definition. The merging of two sorted arrays consisting of k elements takes O(k) time; just
repeatedly choose the lower of the first elements of the two merged parts.
The length of the array is halved on each iteration. In this way, we get consecutive levels
with 1, 2, 4, 8, . . . slices. For each level, the merging of the all consecutive pairs of slices requires
O(n) time. The number of levels is O(log n), so the total time complexity is O(n log n) (read
more at http://en.wikipedia.org/wiki/Merge_sort)."""


t = [5, 2, 8, 14, 1, 16]
selection_sort(t)
counting_sort(t, 16)
