class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            board[r][c] = '#'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr > ROWS-1 or nc > COLS-1 or board[nr][nc] == 'X' or board[nr][nc] == "#":
                    continue
                board[nr][nc] = '#'
                dfs(nr, nc)
 
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = "O"

