"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque
        if not node:
            return None
        
        graph = {node: Node(node.val)}
        q = deque([])
        q.append(node)
        
        while q:
            n = q.popleft()
            # visited.add(node)

            for nig in n.neighbors:
                if nig not in graph:
                    q.append(nig)
                    graph[nig] = Node(nig.val)
                graph[n].neighbors.append(graph[nig])

        return graph[node]