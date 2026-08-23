class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit <= 0:
                l += 1
                r += 1
            r += 1

            maxProfit = max(maxProfit, profit)
        return maxProfit
        