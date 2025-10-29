# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root or (root and not root.left and not root.right):
            return 0

        def cal(root, isleft):
            if not root:
                return 0
            if not root.left and not root.right:
                if isleft:
                    return root.val

            return cal(root.left, True) + cal(root.right, False)
        return cal(root, False)