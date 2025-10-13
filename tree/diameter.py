# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# leetcode 543
# brute force
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ma_d = 0
        def dmeter(root):
            nonlocal ma_d
            if not root:
                return 0
            
            left = dmeter(root.left)
            right = dmeter(root.right)

            ma_d = max(ma_d, left + right)
            return max(left, right) +1
        
        dmeter(root)
        return ma_d