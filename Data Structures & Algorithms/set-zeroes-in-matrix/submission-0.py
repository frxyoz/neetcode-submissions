class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        def update(x, row = True):
            if row:
                for y in range(COLS):
                    matrix[x][y] = 0
            else:
                for i in range(ROWS):
                    matrix[i][x] = 0
        s = []
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    s.append((i, True))
                    s.append((j, False))

        for coord, boo in s:
            update(coord, boo)
        
        
        
        