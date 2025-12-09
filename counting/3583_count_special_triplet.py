class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 +7
        MAXV = max(nums) * 2
        left = [0] * (MAXV + 1)
        right = [0] * (MAXV + 1)

        for x in nums:
            right[x] += 1

        total = 0
        for x in nums:
            right[x] -= 1
            target = x * 2
            if target <= MAXV:
                total += left[target] * right[target]
            left[x] += 1

        return total % mod
