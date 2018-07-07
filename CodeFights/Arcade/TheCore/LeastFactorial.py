import math

# Given an integer n, find the minimal k such that
#
# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.
#
# Example
#
# For n = 17, the output should be
# leastFactorial(n) = 24.
#
# 17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).


def leastFactorial(n):

    # To break out from list comprehension and return only one value use next()
    # with generator expression and default value

    return next((math.factorial(i) for i in range(1, n) if math.factorial(i) >= n), 1)

    # Equivalent :

    # fact = 1
    # for i in range(1,n):
    #     fact *= i
    #     if fact >=n:
    #         break;
    # return fact


print(leastFactorial(120))
