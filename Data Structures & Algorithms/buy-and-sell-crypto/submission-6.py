class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        checked = set([prices[0]])
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - min(checked)
            if profit > max_profit:
                max_profit = profit
            checked.add(prices[i])
        return max_profit

            


    