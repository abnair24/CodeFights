#9, 8, 8, 5, 3, 5, 3, 2, 8, 6

def zigzag(a):
    count = 0
    l = set()

    for i in range(0,len(a)):
        if i==0 and (a[0] < a[1] or a[0] > a[1]):
            count = count + 1
        if i==(len(a)-1) and (a[len(a) - 1] < a[len(a) - 2] or a[len(a) - 1] > a[len(a) - 2]):
            count = count + 1

    for i in range(0,len(a)-1):
        if a[i+1] < a[i] and a[i] > a[i-1] :
            count = count + 1
        elif a[i+1] > a[i] and a[i -1] > a[i]:
            count = count +1
        else:
            l.add(count)
            count = 0
    return max(l)+1 if max(l) %2 !=0 or max(l)==0 else max(l) +2

    # best = 1
    # left = 0
    # while left < len(a):
    #     right = left + 1
    #     while right < len(a):
    #         if right == left + 1:
    #             if a[left] == a[right]:
    #                 break
    #
    #         else:
    #             if ((a[right - 1] - a[right - 2]) *
    #                     (a[right - 1] - a[right]) <= 0):
    #                 break
    #         right += 1
    #     best = max(best, right - left + 1)
    #     left = right
    #     if left < len(a) and a[left - 1] != a[left]:
    #         left -= 1
    #
    # return best - 1


# print(zigzag([2, 1, 4, 4, 1, 4, 4, 1, 2, 0, 1, 0, 0, 3, 1, 3, 4, 1, 3, 4]))
print(zigzag([4,4]))

