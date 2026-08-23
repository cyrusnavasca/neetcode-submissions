class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        window_size = 1
        ans = 0
        while window_size <= len(nums):
            for i in range(len(nums)):
                end = i + window_size
                if end > len(nums):
                    break
                window_sum = sum(nums[i:end])
                if window_sum == k:
                    ans += 1
            window_size += 1
        return ans
