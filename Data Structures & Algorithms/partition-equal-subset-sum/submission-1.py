class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}

        totalSum = sum(nums)
        if totalSum % 2:
            return False

        def dfs(i, sum):
            if (i, sum) in memo:
                return memo[(i, sum)]
            if i >= len(nums):
                return sum == totalSum / 2
            memo[(i, sum)] = dfs(i+1, sum + nums[i]) or dfs(i+1, sum)
            return memo[(i, sum)]

        return dfs(0, 0)