import math

from Utils import isBiggerListIndex, isEqualListIndex, isBiggerNumber, isEqualNumber, swap
# isBiggerListIndex(list,a, b, info) returns true if list[a] > list[b], false otherwise
# isEqualListIndex(list,a, b, info) returns true if list[a] == list[b], false otherwise
# isBiggerNumber(a, b, info) returns true if a > b, false otherwise
# isEqualNumber(a, b, info) returns true if a == b, false otherwise
# swap(list, a, b, info) swaps the position of number on indexes a and b

# The 'info' object is necessery so the number of comparisons and swaps can be tracked

#You program must have a 'func' function, which is the entry point to your algorithm

def partition(lst, low, high, info):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if isBiggerListIndex(lst, j, high, info):
            i += 1
            swap(lst, i, j, info)

    swap(lst, i + 1, high, info)
    return i + 1

def quickSort(lst, low, high, info):
    if isBiggerNumber(high, low, info):
        pivotIndex = partition(lst, low, high, info)
        quickSort(lst, low, pivotIndex - 1, info)
        quickSort(lst, pivotIndex + 1, high, info)

def func(lst, info):
    quickSort(lst, 0, len(lst) - 1, info)