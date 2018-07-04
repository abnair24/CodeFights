def killKthBit(n, k):
    print(bin(n))
    return n if n == 0 or len(bin(n)) < k or bin(n)[2:][-k] == '0' else n ^ int(1 << (k - 1))


print(killKthBit( 2738, 30))
