# plain backtracking without memoization
class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        visited = set()

        def beautiful(cur):
            nonlocal count
            if cur > n:
                count+=1
                return
        
    
            for i in range(1, n+1):
                if i not in visited and (i % cur ==0 or cur % i ==0):
                    visited.add(i)
                    beautiful(cur+1)
                    # backtrack
                    visited.remove(i)
                # else: pruning the wrong branch by skipping
        beautiful(1)
        return count


