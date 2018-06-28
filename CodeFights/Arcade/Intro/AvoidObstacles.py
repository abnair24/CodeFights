# You are given an array of integers representing coordinates of obstacles situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make
# jumps of the same length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example
#
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.


def avoidObstacles(inputArray):
    div = []
    jump = 0
    for i in range(len(inputArray)):
        k = 1
        while k <= inputArray[i]:
            if inputArray[i] % k == 0:
                div.append(k)
            k = k + 1
    div = sorted(list(set(div)))

    for j in range(len(div) - 1):
        if div[j + 1] - div[j] != 1:
            jump = div[j] + 1
            break
        else:
            continue
    if jump == 0:
        jump = div[-1] + 1
    return jump

    # Best solution
    # c = 2
    # div = []
    # while True:
    #     for i in inputArray:
    #         div.append(i%c)
    #     if sorted(div)[0] >0 :
    #         return c
    #     div = []
    #     c =c +1


print(avoidObstacles([19, 32, 11, 23]))
