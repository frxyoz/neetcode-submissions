class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, amt):
            if (i, amt) in memo:
                return memo[(i, amt)]
            if amt == 0:
                return 1
            if amt < 0 or i >= len(coins):
                return 0
            total = dfs(i+1, amt) + dfs(i, amt - coins[i])
            memo[(i, amt)] = total
            return total

        return dfs(0,amount)
        
