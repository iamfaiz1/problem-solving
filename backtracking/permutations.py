class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(idx):
            # basse condition
            if idx == len(nums):
                # print('res:', res)
                res.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                # swapping
                # print("nums:", nums)
                nums[i], nums[idx] = nums[idx], nums[i]

                # exploringg
                backtrack(idx +1)

                # swapping backk
                nums[i], nums[idx] = nums[idx], nums[i]
            
        backtrack(0)
        return res
