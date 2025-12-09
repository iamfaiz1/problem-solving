class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for i in set(s):
            left = s.find(i)
            right = s.rfind(i)

            if left < right:
                count+= len(set(s[left+ 1: right]))
        return count
            