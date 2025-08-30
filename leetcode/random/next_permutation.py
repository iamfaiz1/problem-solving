class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        flag = True
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                x = i
                flag = False
                break
        if flag:
            nums.sort()
            return 

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
                break
        
        # reversing
        left = x+1
        right = len(nums)-1
        while(left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1

        

            




        