class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS):
            for j in range(i+1,COLS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(ROWS):
            for j in range(COLS//2):
                matrix[i][j], matrix[i][COLS-j-1] = matrix[i][COLS-j-1],matrix[i][j]

    
