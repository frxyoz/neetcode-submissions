class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        lenRows = len(grid)
        lenCols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= lenRows or c < 0 or c >= lenCols:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return (1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c+1) + dfs(r, c-1))


        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        
        return maxArea