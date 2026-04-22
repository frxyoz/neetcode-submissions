class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        l, r = 0, 1
        while r < len(prices):
            if l == r and r < len(prices)-1:
                r += 1
                if prices[r] - prices[l] > prof:
                    prof = prices[r] - prices[l]
            elif prices[r] - prices[l] < 0:
                l = r
                r += 1
            else:
                if prices[r] - prices[l] > prof:
                    prof = prices[r] - prices[l]
                r += 1
        return prof

