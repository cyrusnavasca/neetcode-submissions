class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
        # Q1: when is an answer complete? 
            if i == n:
                res.append(sol[:])
                return
            
        # Q2: what choices do i have?
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
        backtrack(0)
        return res

