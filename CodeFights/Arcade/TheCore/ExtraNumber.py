# You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other.
#  What is the value of the third integer?
#
# Example
#
# For a = 2, b = 7 and c = 2, the output should be
# extraNumber(a, b, c) = 7.


def extraNumber(a, b, c):
    return c if a == b else b if a == c else a