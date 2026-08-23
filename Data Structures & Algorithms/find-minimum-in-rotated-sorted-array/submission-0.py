class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] > nums[r]: # we are in the LEFT sorted array
                l = mid + 1
            elif nums[mid] < nums[r]: # we are in the RIGHT sorted array
                r = mid
        return nums[l]

        