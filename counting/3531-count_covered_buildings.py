class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import defaultdict

        y_min = defaultdict(lambda:  float('inf'))   #columns
        x_min = defaultdict(lambda:  float('inf'))   #row
        y_max = defaultdict(lambda: -float('inf'))   #columns
        x_max = defaultdict(lambda: -float('inf'))   #row

        for x, y in buildings:
            y_min[y] = min(y_min[y], x)
            y_max[y] = max(y_max[y], x)

            x_min[x] = min(x_min[x], y)
            x_max[x] = max(x_max[x], y)

        count = 0
        for x, y in buildings:
            if y_min[y] < x < y_max[y] and x_min[x] < y < x_max[x]:
                count+=1
        return count

