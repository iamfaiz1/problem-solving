#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        def helper(arr, li):
            if len(arr)==n:
                li.append("".join(arr))
                return
            
            # including
            arr.append("0")
            helper(arr, li)
            arr.pop()
            
            # exluding
            if not arr or arr[-1]=="0":
                arr.append("1")
                helper(arr, li)
                arr.pop()
                
                
        li = []
        helper([], li)
        
        # print(li)
        return li
    
    # ______________________________________________________________________
    # generate string subset for binary string with no consecutive zeros.
    class Solution:
        def validStrings(self, n: int) -> List[str]:
            res = []
            def helper(arr, flag):
                if len(arr)>=n:
                    res.append("".join(arr))
                    return 
                
                arr.append("1")
                helper(arr, True)
                arr.pop()
                if flag:
                    arr.append("0")
                    helper(arr, False)
                    arr.pop()
            helper([], True)
            return res
                
