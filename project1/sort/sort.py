"""
Sorting algorithms: merge sort and quick sort

Mege sort: requires extra memory to store subarray but is stable
Quick sort: requires no extra memory but is unstable
"""


def mergesort(list, low, high):
    """
    Mege sort algorithm (in-place) via splitting list in half.
    Time complexity: O(nlogn)

    Parameters
    ----------
    list (array): List to sort
    low (int): First index of list, inclusive
    high (int): Second index of list, inclusive

    Return
    ------
    None. List is sorted by reference
    """
    if(low < high):
        mid = (low + high) // 2

        mergesort(list, low, mid)
        mergesort(list, mid + 1, high)
        merge(list, low, mid, high)


def merge(list, low, mid, high):
    """
    Helper function to merge two subarrays into list

    Parameters
    ----------
    list (array): List to sort
    low (int): First index of list, inclusive
    mid (int): Middle index (floor)
    high (int): Second index of list, inclusive

    Return
    ------
    None. Two subarrays are merged to list by reference.
    """
    i, j, k = low, mid + 1, 0
    temp = []

    while(i <= mid and j <= high):
        if(list[i] < list[j]):
            temp.append(list[i])
            i += 1
        else:
            temp.append(list[j])
            j += 1

    if(i > mid):
        while(j <= high):
            temp.append(list[j])
            j += 1
    else:
        while(i <= mid):
            temp.append(list[i])
            i += 1

    for x, y in zip(range(low, high + 1), range(len(temp))):
        list[x] = temp[y]


def quicksort(list, low, high):
    """
    Quick sort algorithm via splitting list in half by pivot point
    Time complexity: A(nlogn), W(n^2)

    Parameters
    ----------
    list (array): List to sort
    low (int): First index of list, inclusive
    high (int): Second index of list, inclusive

    Return
    ------
    None. List is sorted by reference
    """
    if(low < high):
        pivot = partition(list, low, high)
        quicksort(list, low, pivot - 1)
        quicksort(list, pivot + 1, high)


def partition(list, low, high):
    """
    Helper function to place all items less than pivot to left.

    Parameters
    ----------
    list (array): List to sort
    low (int): First index of list, inclusive
    high (int): Second index of list, inclusive

    Return
    ------
    pivot (int): index of pivot
    """
    i, j = low + 1, low
    pivot_item = list[low]

    while(i <= high):
        if(list[i] < pivot_item):
            j += 1
            list[i], list[j] = list[j], list[i]

        i += 1

    pivot = j
    list[low], list[pivot] = list[pivot], list[low]

    return pivot
