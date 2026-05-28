class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        lenRows = len(grid)
        lenCols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= lenRows or c < 0 or c >= lenCols:
                return

            if grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        
        return count
            
