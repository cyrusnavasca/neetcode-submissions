class Solution:
    def climbStairs(self, n: int) -> int:
        # base case(s)
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # recursion
        return (self.climbStairs(n-1) + self.climbStairs(n-2))
        
        