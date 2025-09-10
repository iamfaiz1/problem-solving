# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal
        sizes: List[int] = []

        def postorder(node):
            if not node:
                return 0
            
            left = postorder(node.left)
            right = postorder(node.right)

            if left == right and left != -1:
                size = left+right+1
                sizes.append(size)
                return size
            else:
                return -1
        postorder(root)

        sizes.sort(reverse=True)
        return sizes[k-1] if k <= len(sizes) else -1
        

