class Solution:
    def helper(self, stack, temp):
        if not stack or stack[-1]<temp:
            stack.append(temp)
        else:
            x = stack.pop()
            self.helper(stack, temp)
            stack.append(x)

    def sorting(self,stack):
        if not stack:
            return
        else:
            temp = stack.pop()
            self.sorting(stack)
            self.helper(stack, temp)

stack = [3 ,32, 33,24, 43, 55,1, 3,-2,0]
print(stack)
Solution().sorting(stack)
print(stack)