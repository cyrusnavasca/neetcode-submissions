class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            search = target - nums[i]
            if search in seen:
                return [seen[search], i]
            seen[nums[i]] = i 
        
        # seen = {3: 0}
        # search = 3

