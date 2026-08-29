class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
        # Q1: when is an answer complete
            if len(sol) == n:
                res.append(sol[:])
                return

        # Q2: what choices can we make at each state
            for i in range(n):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack(i+1)
                    sol.pop()

        backtrack(0)
        return res