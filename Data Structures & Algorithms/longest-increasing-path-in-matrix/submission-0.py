class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        l, w = len(matrix), len(matrix[0])
        memo = {}
        highest = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            best = 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if min(nx, ny) >= 0 and nx < l and ny < w:
                    if matrix[nx][ny] > matrix[x][y]:
                        best = max(best, 1 + dfs(nx, ny))
            memo[(x, y)] = best
            return best
        
        for i in range(l):
            for j in range(w):
                highest = max(highest, dfs(i, j))

        return highest
        