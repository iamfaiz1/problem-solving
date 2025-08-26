class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = max(nums)
        m = right

        while left <= right:
            mid = left + (right-left)//2
            count = 0
            for i in nums:
                count += math.ceil(i/mid)
            
            if count <= threshold:
                right = mid-1
                m = mid
            else:
                left = mid+1
        return m
