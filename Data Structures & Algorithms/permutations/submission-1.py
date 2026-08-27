class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []
        used = set()

        def backtrack(i):
            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(n):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                sol.append(nums[i])
                backtrack(i)
                sol.pop()
                used.remove(nums[i])

        backtrack(0)
        return res
        