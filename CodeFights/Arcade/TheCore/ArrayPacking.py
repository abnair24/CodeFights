def arrayPacking(a):
    x=""
    for i in a:
        x = (bin(i)[2:]).zfill(8) + x
    return int(x, 2)

    #     print('{0:032b}'.format(i))

    # Best soln
    #return sum([a[i] << i * 8 for i in range(len(a))])


print(arrayPacking([24, 85, 0]))