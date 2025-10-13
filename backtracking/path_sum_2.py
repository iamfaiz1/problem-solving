# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(arr, s, root):
            if not root:
               return
            
            arr.append(root.val)
            s += root.val

            if (not root.left and
                not root.right and
                s == targetSum ):
                res.append(arr[:])

            helper(arr, s, root.left)
            helper(arr, s, root.right)
            arr.pop() 

        if not root:
            return []
        res = []
        helper([], 0, root)
        return res
