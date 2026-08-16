class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for val in nums:
            if val in checked:
                return True
            else:
                checked.add(val)
        return False

  