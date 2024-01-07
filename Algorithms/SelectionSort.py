import time
from Utils import isBiggerNumber, isBiggerListIndex, isEqualListIndex, isEqualNumber, swap
# isBiggerListIndex(list,a, b, info) returns true if list[a] > list[b], false otherwise
# isEqualListIndex(list,a, b, info) returns true if list[a] == list[b], false otherwise
# isBiggerNumber(a, b, info) returns true if a > b, false otherwise
# isEqualNumber(a, b, info) returns true if a == b, false otherwise
# swap(list, a, b, info) swaps the position of number on indexes a and b

# The 'info' object is necessery so the number of comparisons and swaps can be tracked

#You program must have a 'func' function, which is the entry point to your algorithm
def func(listToSort, info):
    for i, itemI in enumerate(listToSort):
        for j, itemJ in enumerate(listToSort):
            if (isBiggerListIndex(listToSort, i,j, info)):
                swap(listToSort, i, j, info)
                itemI = itemJ
    return