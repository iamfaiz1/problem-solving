from collections import defaultdict

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 +7
        arr.sort()
        di = defaultdict(int)
        for v in arr:
            di[v]= 1
        
        # work
        for i, v in enumerate(arr):
            for j in range(i+1):
                if v % arr[j]==0:
                    b = arr[i] //arr[j]
                    if v% b ==0:
                        di[v] += di[arr[j]] * di[b]
            print(di[v])

        return sum(di.values()) % mod
