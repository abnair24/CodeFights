
# Call two arms equally strong if the heaviest weights they each are able to lift are equal.
#
# Call two people equally strong if their strongest arms are equally strong (the strongest arm can be
# both the right and the left), and so are their weakest arms.
#
# Given your and your friend's arms' lifting capabilities find out if you two are equally strong.
#
# Example
#
# For yourLeft = 10, yourRight = 15, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 10, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = true;
# For yourLeft = 15, yourRight = 10, friendsLeft = 15 and friendsRight = 9, the output should be
# areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight) = false


def are_equally_strong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft == friendsLeft:
        if yourRight == friendsRight:
            return True
        else:
            return False
    elif yourLeft == friendsRight:
        if yourRight == friendsLeft:
            return True
        else:
            return False
    else:
        return False


print(are_equally_strong(10, 15, 15, 10))