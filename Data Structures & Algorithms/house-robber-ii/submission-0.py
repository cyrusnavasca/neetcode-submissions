class Solution:
    def rob(self, nums: List[int]) -> int:

        def original(nums: List[int]) -> int:
            # edge case
            if len(nums) == 1:
                return nums[0]

            # initialize base cases
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            # process
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
            return dp[-1]
        
        rob1 = original(nums[0:len(nums)-1])
        rob2 = original(nums[1:len(nums)])

        return max(rob1, rob2)

        
