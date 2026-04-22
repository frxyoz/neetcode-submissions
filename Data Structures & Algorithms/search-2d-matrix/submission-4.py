class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)
        if target > matrix[b-1][0]:
            t = b-1
        else:
            while t < b:
                m = t + (b - t) // 2
                if matrix[m][0] == target:
                    return True
                elif matrix[m][0] < target:
                    t = m
                else:
                    b = m - 1
        print(str(b))
        l, r = 0, len(matrix[t])-1
        while l <= r:
            m = l + (r - l) // 2
            print(str(matrix[t][m]))
            if matrix[t][m] == target:
                return True
            elif matrix[t][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False