class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount: return 0
        if len(coins) == 1:
            if coins[0] > amount:
                return -1
            
        dp = [float('inf')] * amount
        for coin in coins:
            if coin <= amount:
                dp[coin-1] = 1
        for i in range(amount):
            for coin in coins:
                if i + coin < amount:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
            
        if dp[amount-1] != float('inf'):
            return dp[amount-1]
        return -1