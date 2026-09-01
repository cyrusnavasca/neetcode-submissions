class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            # set current target
            target = i
            current_minimum = math.inf

            for coin in coins:
                # if coin is bigger than target, skip
                if coin > target: 
                    break
                diff = target - coin
                coins_used = 1 + dp[diff]
                current_minimum = min(current_minimum, coins_used)

            dp[i] = current_minimum
        
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]
            
                