class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        
        # 3. Iterate over the lengths of the subarrays (from smallest to largest)
        for length in range(1, n - 1): # Subarray lengths from 1 to original array size
            for l in range(1, n - length):
                r = l + length - 1
                
                # 4. Find the best balloon 'i' to burst LAST in the current window [l, r]
                for i in range(l, r + 1):
                    # Coins gained from bursting i last + left subproblem + right subproblem
                    coins = nums[l-1] * nums[i] * nums[r+1] + dp[l][i-1] + dp[i+1][r]
                    
                    if coins > dp[l][r]:
                        dp[l][r] = coins
                        
        # The answer for the full original array is stored in dp[1][n-2]
        return dp[1][n-2]
