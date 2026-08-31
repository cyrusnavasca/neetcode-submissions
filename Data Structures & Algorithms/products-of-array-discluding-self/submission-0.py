class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1] * len(nums), [1] * len(nums) 


        # generating pre
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]
        
        # generating post
        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        
        
        # generating output
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = pre[i] * post[i]
        
        return output
