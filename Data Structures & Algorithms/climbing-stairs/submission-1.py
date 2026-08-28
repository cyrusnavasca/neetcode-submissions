class Solution:
    def climbStairs(self, n: int) -> int:
        # cache
        memo = {0: 1, 1: 1, 2: 2}

        # base case(s)
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # recursion
        if n in memo:
            return memo[n]
        else:
            memo[n] = (self.climbStairs(n-1) + self.climbStairs(n-2))
            return memo[n]
        
        