import math


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
