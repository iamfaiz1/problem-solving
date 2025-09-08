
# optimised approach using binary search : log(n)
class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        def helper(x):
            return nums[x]-x-1
        
        while(i<=j):
            mid = (i+j)//2
            xx = helper(mid)
            if xx < k:
                i = mid+1
            else:
                j = mid-1
        return k+i