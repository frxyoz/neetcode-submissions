class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lenRows = len(grid)
        lenCols = len(grid[0])

        q = deque()
        time = 0
        visited = set()

        def addCell(r, c):
            if (min(r, c) < 0 or r == lenRows or c == lenCols or grid[r][c] == 2 or grid[r][c] == 0):
                return
            if (r, c) not in visited:
                q.append((r, c))
                visited.add((r, c))
                if grid[r][c] == 1:
                    grid[r][c] = 2

        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == 2:
                        q.append((row, col))
                        visited.add((row, col))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r-1, c)
                addCell(r+1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            if q:
                time += 1
        
        for row in range(lenRows):
            for col in range(lenCols):
                if grid[row][col] == 1:
                    return -1
        
        return time




