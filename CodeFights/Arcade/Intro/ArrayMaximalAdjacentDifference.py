# Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
#
# Example
#
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.


def arrayMaximalAdjacentDifference(inputArray):
    max = 0
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i + 1])
        if diff > max:
            max = diff

    return max