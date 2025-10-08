
# brute force recursion
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        def helper(start):
            if start >= len(s):
                return True
            
            for i in range(start, len(s)+1):
                if s[start: i+1] in words and helper(i+1):
                    return True
            return False
        
        return helper(0)

# _______________________________________________________
# memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = set()
        def helper(start):
            if start >= len(s):
                return True
            
            if start in memo:
                return False
            
            for i in range(start, len(s)+1):
                if s[start: i+1] in words and helper(i+1):
                    return True
            memo.add(start)
            return False
        
        return helper(0)

# _______________________________________________________
# iterative dp
