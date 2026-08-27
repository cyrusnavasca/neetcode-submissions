class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(n):
                sol.append(nums[i])
                backtrack(i)
                sol.pop()

        backtrack(0)
        return res
        