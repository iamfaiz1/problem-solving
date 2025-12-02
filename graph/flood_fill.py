class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        q = deque([])

        m = len(image)
        n = len(image[0])
        original = image[sr][sc]
        
        if original == color:
            return image
            # idk lets see
        
        directions = [
            (1, 0),     #down
            (-1, 0),    #up
            (0, 1),     #right
            (0, -1),    #left
        ]
        image[sr][sc] = color
        q.append((sr, sc))

        while(q):
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = di+i, dj+j
                    if 0<= ni< m and 0<= nj <n and image[ni][nj]== original:
                        image[ni][nj]=color
                        q.append((ni, nj))
        return image
        

        

        