from collections import Counter



def palindrome_rearranging(inputString):
    count =0
    for i in Counter(inputString).values():
        if i % 2 != 0:
            count += 1
    if count > 1 :
        return False
    else:
        return True


    # # d ={}
    # # count =0
    # # for i in inputString:
    # #     d[i] = inputString.count(i)
    # # for j in d.values():
    # #     if j == 1 :
    # #         count = count + 1
    # # if count > 1:
    # #     return False
    # # else:
    # #     return True
    #
    # d = {}
    # count = 0
    # for i in inputString:
    #     d[i] = inputString.count(i)
    # for j in d.values():
    #     if j == 1:
    #         count = count + 1
    # if (len(inputString) % 2 == 0 and count == 1) or (len(inputString) % 2 !=0 and count == 0):
    #     return True
    # elif count > 1:
    #     return False
    # else:
    #     return False


print(palindrome_rearranging("aabb"))
