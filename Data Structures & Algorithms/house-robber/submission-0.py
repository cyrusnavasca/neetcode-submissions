class Solution:
    def rob(self, nums: List[int]) -> int:
        # initialize dp
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]

        # loop
        for i in range(2, n):
            curr_max = max((dp[i-2] + nums[i]), dp[i-1])
            dp[i] = curr_max

        return dp[-1]


        