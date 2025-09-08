class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, ma = 0, 0
        di = {}
        for j, ch in enumerate(s):
            if ch in di and di[ch]>=i:
                i= di[ch] +1
            di[ch] = j
            ma = max(ma, j-i+1)
        
        return ma