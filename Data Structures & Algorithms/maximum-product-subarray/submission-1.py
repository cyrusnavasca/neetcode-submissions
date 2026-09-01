class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = -math.inf

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = math.prod(nums[i:j+1])
                largest = max(largest, prod)
        
        return largest