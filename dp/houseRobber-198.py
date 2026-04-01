class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def solve(i):
            if i>=len(nums):
                return 0

            if i in memo:
                return memo[i]

            else:
                pick = solve(i+2) + nums[i]
                skip = solve(i+1)
                memo[i] = max(pick, skip)
            return memo[i]
        return solve(0)


# ------------------------------------------------------------------
# iterative solution using O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
            
        def solve(nums):
            a = 0
            b = 0
            for i in nums:
                c = max(b, a+i)
                a = b
                b = c
            return b
        
        return solve(nums)
            
