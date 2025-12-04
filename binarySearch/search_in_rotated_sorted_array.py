class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding pivot
        def pivot():
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid  # here we r not doing 'right = mid-1' therefore loop condn is left < right
            return left

        # calculaating target
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        p = pivot()

        # find search space
        if nums[p] <= target <= nums[r]:
            l = p
        else:
            r = p - 1

        # binary seach for target
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# -------------------------------------------------------------------
# approach 2: checking sorted half

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left = 0 
        right = len(nums)-1

        # check left is sorted and right is sorted
        while left <= right:
            mid = (left + right) //2

            if nums[mid] == target:
                return mid
            
            # check left sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid+1
                    
            # check right sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
        return -1


