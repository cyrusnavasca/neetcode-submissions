class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = set([0])
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0:
                    res.add(profit)
        return max(res)

    