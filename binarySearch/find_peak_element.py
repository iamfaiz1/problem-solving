class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        if len(nums)==1:
            return 0
        
        if nums[left]> nums[left+1]:
            return left

        if nums[right]> nums[right-1]:
            return right

        while(left <= right):
            mid = left+(right-left)//2

            if nums[mid-1]< nums[mid] >nums[mid+1]:
                return mid

            elif nums[mid+1] > nums[mid]:
                left = mid+1

            else:
                right = mid-1
        return -1