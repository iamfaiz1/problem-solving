# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # solving in O(n)
        # single inorder traversal
        # i'll use 3 pointers, two for marking those faulty values and 3rd one for comparison
        self.prev_ptr = None
        self.first_num = None
        self.second_num = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev_ptr and self.prev_ptr.val > node.val:
                if not self.first_num:
                    self.first_num = self.prev_ptr
                self.second_num = node
            self.prev_ptr = node

            inorder(node.right)
        # calling
        inorder(root)
        # swapping
        self.first_num.val, self.second_num.val = self.second_num.val, self.first_num.val
        

# bruteForce

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # find inorder 
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        # CALLING first inorder
        inorder(root)
        arr.sort()
        def inorder2(node, i):
            if not node:
                return
            inorder2(node.left, i+1)
            node.val = arr.pop(0)
            inorder2(node.right, i+1)

        inorder2(root, 0)
        


            