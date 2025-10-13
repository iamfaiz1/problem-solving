# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if not root:
                return None
            
            elif root.val==p.val or root.val == q.val:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return None
            elif left and right:
                return root
            elif left:
                return left
            else:
                return right
        return dfs(root)
            
