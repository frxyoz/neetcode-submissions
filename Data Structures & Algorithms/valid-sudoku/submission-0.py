class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            rowdict = set()
            for y in range(len(board[x])):
                if board[x][y].isdigit():
                    if board[x][y] in rowdict:
                        return False
                    rowdict.add(board[x][y])
        for y in range(len(board[0])):
            coldict = set()
            for x in range(len(board)):
                if board[x][y].isdigit():
                    if board[x][y] in coldict:
                        return False
                    coldict.add(board[x][y])
        for x in range(1, len(board), 3):
            for y in range(1, len(board[x]), 3):
                box = set()

                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if board[i][j].isdigit():
                            if board[i][j] in box:
                                return False
                            box.add(board[i][j])
                            print(box)
                
                
        return True