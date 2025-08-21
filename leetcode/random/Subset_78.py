class Solution:
    def sol(self, nums, i, arr, li):
        if i>=len(nums):
            li.append(arr[:])
            return
        
        # including
        arr.append(nums[i])
        self.sol(nums, i+1, arr, li)

        # excluding
        arr.pop()
        self.sol(nums, i+1, arr, li)
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        li = []
        self.sol(nums,0, [], li)
        return li

    