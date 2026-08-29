class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtrack(i):
            # Q1: when is an answer complete?
            if i == len(nums):
                res.append(sol[:])
                return 
            
            # Q2: what choices do we have at each state?

            # dont pick i
            backtrack(i+1)

            # pick i
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res