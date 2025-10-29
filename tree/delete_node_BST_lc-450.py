# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # preorder
        def helper(root, key):
            # base case
            if not root:
                return root
            
            # to move to correct loaction
            if root.val > key:
                root.left = helper(root.left, key)
            elif root.val < key:
                root.right = helper(root.right, key)
            # found the key
            else:
                # root.val == key

                # its leaf-node
                if not root.left and not root.right:
                    return None

                # have 1 child
                elif not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                    
                # has both child
                else:
                    node = find_predicessor(root.left)
                    root.val = node.val
                    # fixing the modified subtree
                    root.left = helper(root.left, node.val)
            return root

        # finding largest element from left sub tree to replace with
        def find_predicessor(root):
            while root.right:
                root = root.right
            return root
        
        # calling
        return helper(root, key)