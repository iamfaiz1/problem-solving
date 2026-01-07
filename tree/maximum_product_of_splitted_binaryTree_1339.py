# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10**9 +7
        self.ans = 0

        # total sum
        def dfs(node):
            if not node:
                return 0
            return node.val + dfs(node.left)+ dfs(node.right)
 
        total = dfs(root)
        def find(node):
            if not node:
                return 0

            sub = find(node.left) +find(node.right) +node.val
            self.ans = max(self.ans, sub*(total-sub))
            return sub
        
        find(root)
        return self.ans % mod


