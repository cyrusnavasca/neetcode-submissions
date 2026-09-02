class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for num in nums:
            # edge case: element is 0
            if num == 0:
                curr_min, curr_max = 1, 1
            
            # otherwise, proceed
            prev_max = curr_max
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(num * prev_max, num * curr_min, num)

            res = max(res, curr_max)
        
        return res

