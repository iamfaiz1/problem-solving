# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if not root:
                return (0, -float('inf'))
                # root-node sum, node-node subtree sum
            
            leftsum1, leftsum2 = solve(root.left)
            rightsum1, rightsum2 = solve(root.right)

            # ignore negative paths
            leftsum1 = max(leftsum1, 0)
            rightsum1 = max(rightsum1, 0)

            rootsum = max(leftsum1, rightsum1) + root.val
            nodesum = max(
                leftsum2, 
                rightsum2, 
                leftsum1 + rightsum1 + root.val)
            return rootsum, nodesum

        _ , ans = solve(root)
        return ans

