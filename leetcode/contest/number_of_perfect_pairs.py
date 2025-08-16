class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        count  =0
        nums = [abs(x) for x in nums]
        nums.sort()
        # print(nums)
        j=0
        for i in range(len(nums)-1):
            while( j< len(nums) and nums[j]<= nums[i]*2):
                j+=1
            count += (j-i-1)
            
        return count