''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''

#   recursive approach
#   time: O(h), space: O(h)
class Solution:
    def findCeil(self,root, x):
        # code here
        res = -1
        def solve(root):
            nonlocal res
            if not root:
                return
            
            if root.data > x:
                res = root.data
                solve(root.left)
                
            elif root.data < x:
                solve(root.right)
                
            else:
                res = root.data
                return
            return
        solve(root)
        return res

#   iterative approach
''' class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''

#   time: O(h), space: O(1)
class Solution:
    def findCeil(self,root, x):
        # code here
        res = -1
        cur = root
        while(cur):
            if cur.data == x:
                return cur.data
            elif cur.data > x:
                res = cur.data
                cur = cur.left
            else:
                cur = cur.right
                
        return res

# _____________________________________________________________________
# floor in BST
class Solution:
    def floor(self, root, x):
        # Code her
        res = -1
        
        def sol(root):
            nonlocal res
            if not root:
                return 
            
            if root.data > x:
                sol(root.left)
            elif root.data < x:
                res = root.data
                sol(root.right)
            else:
                res = root.data
                return
        
        sol(root)
        return res