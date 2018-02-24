# You are given a two-digit integer n. Return the sum of its digits.


def addTwoDigits(n):
    return int(n/10 + n%10)


number=int(input())
print(addTwoDigits(number))