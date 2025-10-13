# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # applying level order traversal using distance map
        if not root:
            return []
        
        queue = deque()
        queue.append((root, 0, 0))  #node, column_distance, row_distance
        di = defaultdict(list)
        
        while(queue):
            node, col, row = queue.popleft()
            di[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, col-1, row+1))
            if node.right:
                queue.append((node.right, col+1, row+1))
        res =[]
        for d in sorted(di.keys()):
            di[d].sort(key=lambda x: (x[0], x[1]))
            # (x[0], x[1]) sort by row but if col is same row is same then sort by value       
            temp = []
            for row, val in di[d]:
                temp.append(val)
            res.append(temp) 
        return res
            
            
