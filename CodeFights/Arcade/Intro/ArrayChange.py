def array_change(inp):
    count = 0
    for i in range(len(inp) - 1):
        if inp[i] >= inp[i + 1]:
            diff = abs(inp[i] - inp[i + 1])
            count = diff + count + 1
            inp[i + 1] = diff + 1 + inp[i + 1]

    return count


print(array_change([1, 1, 1]))
