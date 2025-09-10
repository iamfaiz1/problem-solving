# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        summ = 0

        # right node left
        def reverseInorder(node):
            nonlocal summ

            if not node:
                return 
            
            # right
            reverseInorder(node.right)

            # node
            summ += node.val
            node.val = summ

            # left
            reverseInorder(node.left)

        reverseInorder(root)
        return root