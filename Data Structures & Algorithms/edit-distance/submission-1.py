class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf') for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j

        def bt(x, y):
            if dp[x][y] != float('inf'):
                return dp[x][y]
            if word1[x-1] == word2[y-1]:
                dp[x][y] = bt(x-1, y-1)
                return dp[x][y]
            else:
                dp[x][y] = min(1 + bt(x-1, y), 1 + bt(x,y-1), 1+bt(x-1, y-1))
                return dp[x][y]

        return bt(len(word1), len(word2))