# to reverse a stack using recursion only

class Solution:
    def ap(self, stack, temp):
        # appends the element in beginneing
        if not stack:
            stack.append(temp)
        else:
            x = stack.pop()
            self.ap(stack, temp)
            stack.append(x)
        
    def reverse(self,stack): 
        #code here
        if not stack:
            return 
        temp = stack.pop()
        self.reverse(stack)
        self.ap(stack, temp)

stack = [3,4,2,5,5,0]
print(stack)
obj = Solution()
obj.reverse(stack)
# reverse(stack)
print(stack)