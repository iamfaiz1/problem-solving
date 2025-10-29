# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        from collections import deque
        def check(root):
            if not root:
                return False
            
            q = deque()
            q.append((root, None))
            while(q):
                size = len(q)
                flag = False
                for _ in range(size):
                    node, parent = q.popleft()
                    if (node.val == x or node.val ==y) and not flag:
                        tp = parent
                        flag = True
                    if (node.val == x or node.val ==y) and flag and tp != parent:
                        return True
                    if node.left:
                        q.append((node.left, node))
                    if node.right:
                        q.append((node.right, node))
            return False
        return check(root)
                    


            

            
            
