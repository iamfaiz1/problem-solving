# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # applying post order : left-right-node
        # temp = TreeNode()
        def invert(root):
            # nonlocal temp
            if not root:
                return
            
            invert(root.left)
            invert(root.right)

            # apply sol
            # temp = root.left
            root.left ,root.right = root.right, root.left
        invert(root)
        return root
    

# pre order willl be slightly fasterr as we can swap while going down the tree
# but post order is more intuitive as we swap while coming back up the tree