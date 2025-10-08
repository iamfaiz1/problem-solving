# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:       
        def sol(root):
            if not root:
                return nn

            if val > root.val:
                if root.right:
                    sol(root.right)
                else:
                    root.right = nn
            else:
                if root.left:
                    sol(root.left)
                else:
                    root.left = nn
         
        nn = TreeNode(val)
        if not root:
            return nn
        sol(root)
        return root
