'''
GFG
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        # code here
        if not root:
            return []
    
        q = deque()
        q.append((root, 0))
        top = {}
        mind = maxd = 0
        
        while(q):
            node, hd = q.popleft()
            
            if hd not in top:
                top[hd] = node.data
            
            if node.left:
                q.append((node.left, hd-1))
                mind = min(mind, hd-1)
            if node.right:
                q.append((node.right, hd+1))
                maxd = max(maxd, hd+1)
        
        res=[]
        for hd in range(mind, maxd+1):
            res.append(top[hd])
        return res


# ___________________________________________________________________________

# bottom view problem using same approach: GFG
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        from collections import deque, defaultdict
        # code here
        def bottom(root):
            if not root:
                return
            
            q = deque()
            q.append((root, 0))
            di = defaultdict(int)
            
            while(q):
                node, distance = q.popleft()
                di[distance] = node.data
                
                if node.left:
                    q.append((node.left, distance-1))
                if node.right:
                    q.append((node.right, distance+1))
            
            ans = []
            for d in sorted(di.keys()):
                ans.append(di[d])
            return ans
        return bottom(root)
        
        