class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = prices[0]
        high = prices[0]

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = prices[i]

            if prices[i] > high:
                high = prices[i]

        return high - low