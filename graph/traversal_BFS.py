from collections import deque
def bfs_traversal(graph, root) -> None:
    # using queue for BFS
    q = deque()
    q.append(root)

    # to track visited nodes
    visited = set()
    visited.add(root)
    
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

        for nodes in graph[node]:
            if nodes not in visited:
                q.append(nodes)

# _____________________________ testing
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9, 10],
    6: [3, 11],
    7: [3, 12, 13],
    8: [4, 14],
    9: [5, 15],
    10: [5, 16],
    11: [6, 17],
    12: [7],
    13: [7, 18],
    14: [8, 19],
    15: [9],
    16: [10],
    17: [11],
    18: [13],
    19: [14]
}

bfs_traversal(graph, 0)