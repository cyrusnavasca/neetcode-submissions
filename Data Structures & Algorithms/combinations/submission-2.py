class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n+1)
        res, sol = [], []

        def backtrack(i):
        # Q1: when is an answer complete
            if i == n:
                if len(sol) == k:
                    res.append(sol[:])
                return

        # Q2: what choices do we have at each state?

            # don't pick i
            backtrack(i+1)

            # pick i
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)

        return res



