class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = set()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                res.add(prices[j] - prices[i])
        if max(res) > 0:
            return max(res)
        else:
            return 0
    