class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, total, combination):
            if total == n and len(combination) == k:
                res.append(combination[:])
            
            elif total>n or len(combination)>k:
                return
            
            for i in range(start, 10):
                combination.append(i)
                backtrack(i+1, total+i, combination)
                combination.pop()
        backtrack(1, 0, [])
        return res
