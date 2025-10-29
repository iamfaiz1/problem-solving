"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        # start by level order traversal
        def Traversal(root):
            if not root:
                return

            q = deque()
            q.append(root)
            while(q):
                c = size = len(q)
                # c counts if how many elements are left in a level so we can assign null to the last pointer
                for _ in range(size):
                    node = q.popleft()
                    c-=1
                    node.next = q[0] if c>0 else None

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return root
        return Traversal(root)
                
# this works for both perfect and non perfect binary trees
# leetcode 116 and 117