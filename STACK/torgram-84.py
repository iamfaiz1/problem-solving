class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # nearest smaller to left
        # nearest smaller to right
        nsl = [0]*n
        nsr = [0]*n
        area = 0

        # Find NSL
        stack = []  #(height, index)
        for i in range(n):
            while stack and heights[i] <= stack[-1][0] :
                stack.pop()
            if not stack:
                nsl[i] = -1
            else:
                nsl[i] = stack[-1][1]
            stack.append((heights[i], i))  # push AFTER processing

        # Find NSR
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= stack[-1][0]:
                stack.pop()
            if not stack:
                nsr[i] = n
            else: 
                nsr[i] = stack[-1][1]
            stack.append((heights[i], i))

        # Compute max area
        for i in range(n):
            width = nsr[i] - nsl[i] - 1
            area = max(area, heights[i] * width)

        return area
