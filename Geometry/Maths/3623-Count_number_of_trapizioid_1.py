class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7

        y_frq = {}
        for _, y in points:
            y_frq[y] = y_frq.get(y, 0) +1
            # finding common y-points because line would be parallel and horizontal
        
        result = 0
        prev = 0
        # applying only permutation and combination pNc
        for y in y_frq.values():
            horizontal = y*(y-1)//2
            result += horizontal * prev
            prev += horizontal
            
        return result % mod
            