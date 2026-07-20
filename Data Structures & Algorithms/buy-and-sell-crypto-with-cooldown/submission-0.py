class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        # Initialize states for day 0
        hold = -prices[0]
        reset = 0
        cooldown = float('-inf')
        
        for i in range(1, len(prices)):
            next_hold = max(hold, reset - prices[i])
            next_cooldown = hold + prices[i]
            next_reset = max(reset, cooldown)
            
            hold, cooldown, reset = next_hold, next_cooldown, next_reset
            
        return max(reset, cooldown)