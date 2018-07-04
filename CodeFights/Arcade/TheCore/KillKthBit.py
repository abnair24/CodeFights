def killKthBit(n, k):
    y = bin(n)[2:]
    x = y[-(k)]
    print(x)
    if x == 1:
        b1 = int(1 << (k-1))
        print(b1)
        return n ^ b1
    else:
        return n


print(killKthBit(37, 4))
