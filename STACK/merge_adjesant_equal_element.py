
from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            if not stack or stack[-1]!=i:
                stack.append(i)
            elif stack and stack[-1]==i:
                stack[-1]+=i
                
            while len(stack)>1 and stack[-1]==stack[-2]:
                stack[-2] += stack[-1]
                stack.pop()
        return stack
            