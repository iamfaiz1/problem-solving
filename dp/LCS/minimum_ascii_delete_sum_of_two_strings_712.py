class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        total_cost = 0
        for c in s1+s2:
            total_cost += ord(c)
        # print(total_cost)

        @lru_cache(None)
        def lcs(i, j):
            if i<0 or j<0:
                return 0
            
            if s1[i]==s2[j]:
                return lcs(i-1, j-1) + ord(s1[i])
            
            else:
                return max(lcs(i-1, j), lcs(i, j-1))
        
        lcs_cost = lcs(len(s1)-1, len(s2)-1)
        return total_cost - 2*lcs_cost