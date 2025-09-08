class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        di={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []

        def backtrack(idx, string):
            if idx == len(digits):
                res.append("".join(string))
                return
            
            dg = digits[idx] 
            # digits = "23"
            # dg = 2
            # dg = 3
            for ch in di[dg]:
                string.append(ch)
                backtrack(idx+1, string)
                string.pop()
        backtrack(0, [])
        return res
