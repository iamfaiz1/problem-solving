class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, arr, summ):
            
            if summ == target:
                res.append(arr[:])
                return

            if summ > target:
                return

            # print(candidates[idx], arr)
            for i in range(idx, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, arr, summ + candidates[i])
                arr.pop()
        backtrack(0, [], 0)
        return res
        