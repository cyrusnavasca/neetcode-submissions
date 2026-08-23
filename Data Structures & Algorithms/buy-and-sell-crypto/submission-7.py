class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > maxProfit:
                maxProfit = profit
            if profit < 0: # unprofitable, need to shift window
                l, r = l+1, r+1
            else:
                r += 1
        return maxProfit

        