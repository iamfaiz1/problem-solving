class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        # edge case

        left = min(bloomDay)
        right = max(bloomDay)
        res = -1

        while(left <= right):
            mid = left + (right-left)//2
            
            # logic for calculations
            # improveddd
            bouquets = 0
            flower_counts = 0
            for b in bloomDay:
                if b<=mid:
                    flower_counts+=1

                    # it will check when above condition is true
                    if flower_counts == k:
                        bouquets +=1
                        flower_counts = 0

                        if bouquets >=m:
                            break
                # resets count cox flowers were non-consecutive
                else:
                    flower_counts = 0

            # logic for binary search
            if bouquets < m:
                left = mid+1
            else:
                right = mid-1
                res = mid

        return res
