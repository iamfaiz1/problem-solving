
# SOLUTION - 3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        s = set()
        def backtrack(idx , arr, summ):
            if summ > target:
                return

            elif summ == target and (tuple(arr) not in s):
                s.add(tuple(arr))
                res.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                backtrack(i+1, arr, summ + candidates[i])
                arr.pop()

        backtrack(0, [], 0)
        return res



# SOLUTION - 3
# optimal without using set
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(idx , arr, summ):
            if summ > target:
                return

            elif summ == target:
                res.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                if i> idx and candidates[i]==candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, arr, summ + candidates[i])
                arr.pop()

        backtrack(0, [], 0)
        return res


# SOLUTION - 3
# more refined version by early breaking
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(idx , arr, remaining):
            if remaining == 0:
                res.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                
                if candidates[i]> remaining:
                    break
                arr.append(candidates[i])
                backtrack(i+1, arr, remaining - candidates[i])
                arr.pop()

        backtrack(0, [], target)
        return res