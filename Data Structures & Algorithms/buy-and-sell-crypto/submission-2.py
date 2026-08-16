class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # store profit rather than just lows and highs

        low = prices[0]
        high = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
                high = prices[i]

            if prices[i] > high:
                high = prices[i]

            if high - low > profit:
                profit = high - low
                

        return profit