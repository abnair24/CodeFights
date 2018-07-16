# Given an integer size, return an array containing each integer from 1 to size in the following order:
#
# 1, size, 2, size - 1, 3, size - 2, 4, ...
#
# Example
#
# For size = 7, the output should be
# constructArray(size) = [1, 7, 2, 6, 3, 5, 4].


def constructArray(size):
    lst = []
    j = 1

    for i in range(0, size, 2):
        lst.append(j)
        j = j+1
    for k in range(1, size, 2):
        lst.insert(k,size)
        size = size - 1
    return lst


print(constructArray(7))


