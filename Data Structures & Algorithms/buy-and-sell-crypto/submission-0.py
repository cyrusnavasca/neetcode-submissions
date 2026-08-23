class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        high = 0
        low = prices[0]
        for i in range(len(prices)):
            # Check for minimum & reset max if neeeded
            if prices[i] < low:
                low = prices[i]
                high = 0

            # Check for maximum
            if prices[i] > high:
                high = prices[i]

        return high - low

            

        