import time
import math
from Utils import isBiggerNumber, isBiggerListIndex, isEqualListIndex, isEqualNumber, swap
# isBiggerListIndex(list,a, b, info) returns true if list[a] > list[b], false otherwise
# isEqualListIndex(list,a, b, info) returns true if list[a] == list[b], false otherwise
# isBiggerNumber(a, b, info) returns true if a > b, false otherwise
# isEqualNumber(a, b, info) returns true if a == b, false otherwise
# swap(list, a, b, info) swaps the position of number on indexes a and b

# The 'info' object is necessery so the number of comparisons and swaps can be tracked

#You program must have a 'func' function, which is the entry point to your algorithm
def merge(listToSort, start1, end1, start2, end2, info):
    size1 = end1 - start1 + 1
    size2 = end2 - start2 + 1
    while isBiggerNumber( size1, 0, info) and isBiggerNumber(size2, 0, info):
        if isBiggerListIndex(listToSort, start1, start2, info):
            start1 = start1 + 1
            size1 = size1 - 1
        else:
            swap(listToSort, end1, start2, info)
            pointer = end1 - 1
            # while isBiggerNumber(pointer + 1, start1, info):
            while pointer + 1 > start1:
                swap(listToSort, pointer, pointer + 1, info) 
                pointer = pointer - 1
            start1 = start1 + 1
            end1 = end1 + 1
            start2 = start2 + 1
            size2 = size2 - 1
    return



def mergeSort(listToSort, start, end, info):
    if isEqualNumber(start, end, info):
        return
    mergeSort(listToSort, start, math.floor(((end - start) / 2) + start), info)
    mergeSort(listToSort, math.ceil(((end - start) / 2) + start), end, info)
    merge(listToSort, start, math.floor(((end - start) / 2) + start), math.ceil(((end - start) / 2) + start), end, info)
    return 

def func(listToSort, info):
    # print("Antes: " + str(listToSort) + "\n\n")
    mergeSort(listToSort, 0, len(listToSort) - 1, info)
    # print("Depois: " + str(listToSort))
    return


