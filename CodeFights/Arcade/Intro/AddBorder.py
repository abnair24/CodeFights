# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
#
# Example
#
# For
#
# picture = ["abc",
#            "ded"]
# the output should be
#
# addBorder(picture) = ["*****",
#                       "*abc*",
#                       "*ded*",
#                       "*****"]


def add_border(input):
    l = len(input[0]) * 2
    return ["*" * l] + [x.center(l, "*") for x in input] + ["*" * l]


print(add_border(["yhopw", "hpplz", "idbnb", "*wehb", "swbbg"]))
