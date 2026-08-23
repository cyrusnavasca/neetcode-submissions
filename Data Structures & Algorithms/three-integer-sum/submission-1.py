class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            seen = set()
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)):
                search = -(nums[i] + nums[j])
                if search in seen:
                    ans.append([nums[i], nums[j], search])
                seen.add(nums[j])
        return ans

