# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def post_order(root):
            if not root:
                return (0, None)
            
            l_depth, l_node = post_order(root.left)
            r_depth, r_node = post_order(root.right)

            if l_depth > r_depth:
                return (l_depth +1, l_node)

            if l_depth < r_depth:
                return (r_depth +1, r_node)
            
            else:
                return (l_depth +1, root)
        
        return post_order(root)[1]
            
# approach:

# applying post order and bubling out the depth and node info:
# the resting node is passed to the parent node

# conditions:
    # if left and right depth are same return current node
    # if left depth is greater return left node
    # if right depth is greater return right node

# finally return the node info from root
