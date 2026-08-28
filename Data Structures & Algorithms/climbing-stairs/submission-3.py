class Solution:
    def climbStairs(self, n: int) -> int:
        # cache
        memo = {0: 1, 1: 1, 2: 2}
        
        # recursion
        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = (f(n-1) + f(n-2))
                return memo[n]
        
        return f(n)
        
        