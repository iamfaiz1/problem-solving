# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def pre_order(root):
            if not root:
                return 
            
            if root.val < low:
                return pre_order(root.right)
            elif root.val > high:
                return pre_order(root.left)
                
            
            root.left = pre_order(root.left)
            root.right =  pre_order(root.right)

            return root

        return pre_order(root)


        