from typing import List

def findWays(arr: List[int], k: int) -> int:
    c = 0
    memo = {}
    mod = 10**9+7

    def helper(i, count):
        nonlocal c
        nonlocal mod

        # prune: if count already exceeded k, stop
        if count > k:
            return 0

        if (i, count) in memo:
            return memo[(i, count)]

        if i==len(arr):
            return 1 if count == k else 0

        # include + exclude
        res = helper(i+1, count+ arr[i]) + helper( i+1, count)
        res %= mod
        memo[i, count] = res

        return res
    
    return helper(0, 0) 
