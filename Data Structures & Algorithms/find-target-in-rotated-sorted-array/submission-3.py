class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            # LEFT SIDE
            if nums[mid] > nums[r]:
                # easy scenario
                if target > nums[mid]:
                    l = mid + 1
                # hard scenario
                else:
                    r = mid - 1
            # RIGHT SIDE
            else:
                # easy scenario
                if nums[mid] < nums[r]:
                    r = mid - 1
                # hard scenario
                else:
                    l = mid + 1

        return -1
