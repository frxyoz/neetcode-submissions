class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while True:
            oldCost, x, y = heapq.heappop(heap)
            if x == m-1 and y == n-1:
                return oldCost
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in dirs:
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                    if (x + dx, y + dy) not in visited:
                        newCost = max(oldCost, grid[x + dx][y + dy])
                        heapq.heappush(heap, (newCost, x + dx, y + dy))
            


        return heapq.heappop(heap)[0]