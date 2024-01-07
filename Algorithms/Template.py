from Utils import isBiggerListIndex, isEqualListIndex, isBiggerNumber, isEqualNumber, swap
# isBiggerListIndex(list,a, b, info) returns true if list[a] > list[b], false otherwise
# isEqualListIndex(list,a, b, info) returns true if list[a] == list[b], false otherwise
# isBiggerNumber(a, b, info) returns true if a > b, false otherwise
# isEqualNumber(a, b, info) returns true if a == b, false otherwise
# swap(list, a, b, info) swaps the position of number on indexes a and b

# The 'info' object is necessery so the number of comparisons and swaps can be tracked

#You program must have a 'func' function, which is the entry point to your algorithm
def func(listToSort, info):
    #Sort the provided list
    return