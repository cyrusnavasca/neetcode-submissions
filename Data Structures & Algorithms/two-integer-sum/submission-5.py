class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, val in enumerate(nums):
            search = target - val
            if search in seen:
                return [seen[search], i]
            seen[val] = i
        