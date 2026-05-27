class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cur = ["." * n for _ in range(n)]
        cols = set()
        posDiag = set() # c - r is the same
        negDiag = set() # c + r is the same

        def backtrack(i):
            if i == n:
                res.append(cur[:])
                return
            for col in range(n):
                if col not in cols and i - col not in posDiag and i + col not in negDiag:
                    cur[i] = cur[i][:col] + "Q" + cur[i][col+1:]
                    cols.add(col)
                    posDiag.add(i - col)
                    negDiag.add(i + col)

                    backtrack(i+1)

                    cur[i] = "." * n
                    cols.remove(col)
                    posDiag.remove(i - col)
                    negDiag.remove(i + col)

        backtrack(0)
        return res