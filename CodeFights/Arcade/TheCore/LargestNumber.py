# Given an integer n, return the largest number that contains exactly n digits.
#
# Example
#
# For n = 2, the output should be
# largestNumber(n) = 99.


def largestNumber(n):
    num = ""
    for i in range(0,n):
        num = num + "9"
    return int(num)


number = int(input())
print(largestNumber(number))
