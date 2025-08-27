class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []
        result = []
        def helper(opened, closed):
            if opened == closed == n:
                result.append("".join(arr))
                return
            
            # opening parentheses condition
            if opened <n:
                arr.append("(")
                helper(opened+1, closed)
                arr.pop()

            if closed < opened:
                arr.append(")")
                helper(opened, closed+1)
                arr.pop()
        helper(0, 0)
        return result

# can be optimised slightly
# we can use string instead of arr

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(s, opened, closed):
            if opened == closed == n:
                result.append(s[:])
                return
            
            # opening parentheses condition
            if opened <n:
                helper(s+"(", opened+1, closed)

            if closed < opened:
                helper(s+")", opened, closed+1)
        helper("", 0, 0)
        return result
