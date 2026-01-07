class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [float('inf')] * n

        # Pass 1: left → right
        prev = -float('inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        # Pass 2: right → left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
    
# ----------------------------------------------------------------------------------
# --                     bruteforece: doule loop (passed)                         --

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        el = []
        for i, ch in enumerate(s):
            if ch==c:
                el.append(i)
        
        ans = [0]*len(s)

        for i, ch in enumerate(s):
            ans[i] = min(abs(x - i) for x in el)
        return ans
        