class Solution:
    def countTriples(self, n: int) -> int:
        max_sq = n * n

        isSquare = [False] * (max_sq + 1)
        for x in range(1, n + 1):
            isSquare[x * x] = True
        
        count = 0

        for i in range(1, n):
            i2 = i * i
            for j in range(i + 1, n):
                s = i2 + j * j
                # FIX: Check if sum exceeds n^2 before accessing the list
                if s <= max_sq and isSquare[s]:
                    count += 2
                    
        return count