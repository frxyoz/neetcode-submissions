class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * (len(nums)+1) for _ in range(len(nums))]
        longest = 0

        def dfs(i, j):
            if i >= len(nums):
                return 0
            if dp[i][j+1] != -1:
                return dp[i][j+1]
            if j == -1 or nums[i] > nums[j]:
                dp[i][j+1] = max(dfs(i+1, i)+1, dfs(i+1,j))
                return dp[i][j+1]
            else:
                dp[i][j+1] = dfs(i+1,j)
                return dp[i][j+1]

        return dfs(0, -1)
            
            