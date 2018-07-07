def countSumOfTwoRepresentations2(n, l, r):

    # return len ({ frozenset(p) for p in [(i, n-i) for i in range(l,r+1) if l <= n-i <= r ] })
    return len({tuple(sorted(p)) for p in [(i, n-i) for i in range(l, r+1) if l <= n-i <= r]})



print(countSumOfTwoRepresentations2(6,2,4))
