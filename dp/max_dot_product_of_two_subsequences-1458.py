class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        @lru_cache(None)
        def solve(i, j):
            if i<0 or j<0:
                return -float('inf')
            
            product = nums1[i] * nums2[j]
            
            return max(
                product,
                product + solve(i-1, j-1),
                
                solve(i, j-1),
                solve(i-1, j)
            )
        return solve(len(nums1)-1, len(nums2)-1)
        