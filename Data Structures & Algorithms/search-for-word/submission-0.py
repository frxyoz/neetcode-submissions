class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        res = False
        
        def backtrack(x, y, word):
            nonlocal res
            if not word:
                res = True
                return
            if x >= height or x < 0 or y >= width or y < 0 or board[x][y] != word[0]:
                return
            temp = board[x][y]
            board[x][y] = '#'
            backtrack(x+1, y, word[1:])
            backtrack(x-1, y, word[1:])
            backtrack(x, y+1, word[1:])
            backtrack(x, y-1, word[1:])
            board[x][y] = temp

        for i in range(height):
            for j in range(width):
                backtrack(i, j, word)

        return res
        