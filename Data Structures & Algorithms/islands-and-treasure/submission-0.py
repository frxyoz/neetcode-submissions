class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        lenRows = len(grid)
        lenCols = len(grid[0])

        def dfs(r, c, dist):
            if r < 0 or r >= lenRows or c < 0 or c >= lenCols or grid[r][c] == -1:
                return
            if dist > grid[r][c]:
                return
            grid[r][c] = dist
            dfs(r+1, c, dist+1)
            dfs(r-1, c, dist+1)
            dfs(r, c-1, dist+1)
            dfs(r, c+1, dist+1)
        
            

        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)
        

