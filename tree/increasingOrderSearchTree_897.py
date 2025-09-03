# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # optimised approach
        # usnig same tree by modifying existing tree
        # traverse inroder and modify tree after base case

        dummy = TreeNode(-1)
        self.current = dummy

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            # modifying
            self.current.right = node
            node.left = None
            self.current = node

            inorder(node.right)

        inorder(root)
        return dummy.right
