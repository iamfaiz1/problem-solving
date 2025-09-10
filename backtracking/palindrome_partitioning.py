class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palind(string):
            return string == string[::-1]
        
        def backtrack(arr, start):
            if start >= len(s):
                res.append(arr[:])
                return
            
            for i in range(start, len(s)):
                temp_s = s[start:i+1]
                # print(temp_s)
                if palind(temp_s):
                    arr.append(temp_s)
                    backtrack(arr, i+1)
                    arr.pop()
        
        res = []
        backtrack([], 0)
        return res

# could have used 2 pointer for palindrome check




# dynamic programming using dictionary to store palindrome substringsfrom typing import List in
#  order n2
from collections import defaultdict
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = defaultdict(bool)

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    dp[(i, j)] = True


        def backtrack(arr, start):
            if start >= len(s):
                res.append(arr[:])
                return
            
            for i in range(start, len(s)):
                temp_s = s[start:i+1]

                if dp[(start, i)]:
                    arr.append(temp_s)
                    backtrack(arr, i+1)
                    arr.pop()
        
        res = []
        backtrack([], 0)
        return res