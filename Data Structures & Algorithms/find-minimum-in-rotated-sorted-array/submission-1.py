class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l != r:
            # 1) calculate midpoint
            mid = l + ((r - l)//2)

            # 2) find what side we are on, and handle accordingly
            # Case 1: LEFT SIDE 
            if nums[mid] > nums[r]:
                l = mid + 1
            # Case 2: RIGHT SIDE
            else:
                r = mid
        
        return nums[r]


        