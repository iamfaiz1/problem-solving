
from typing import List


class Solution:
    def checkSubsequenceSum(self, N, arr, k):
        # Check if there is a subsequence with sum equal to k
        def helper(count, i):
            if count == k:
                return True
            
            if count>k:
                return False
                
            if i>= len(arr):
                return False
            
            # print(count, arr[i])
            if helper(count + arr[i], i+1):
                return True
            
            elif helper(count , i+1):
                return True
            
            return False
        
        return helper(0, 0)

    from typing import List


# coding ninja problem // naukri.com
def findWays(arr: List[int], k: int) -> int:
    c = 0
        # stores count of such subsequences
        # Count the number of subsequences with sum equal to k
    def helper(arr, i, count):
        nonlocal c

        if count == k:
            c += 1
            return

        if count >  k:
            return 
        
        if i>= len(arr):
            return 
        
        # print(c, count, arr[i])
        # including
        helper(arr, i+1, count + arr[i])

        # not including
        helper(arr, i+1, count)

    helper(arr, 0, 0)
    return c