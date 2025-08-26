class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1
        speed = 1

        while (left <= right):
            mid = left + (right-left)//2
            bc = 0
            # calculation
            for i in piles:
                bc += math.ceil(i/mid)

            if bc > h:
                speed = max(speed, mid+1)
                left = mid +1
            else:
                right = mid -1

        return speed
