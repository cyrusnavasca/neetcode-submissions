class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        def backtrack(i):
            # Q1: when is an answer complete? (sum >= target)
            if sum(sol) == target:
                res.append(sol[:])
                return
            elif i == len(nums) or sum(sol) > target:
                return
            
            # Q2: what choices do i have?
            # don't pick i

            backtrack(i+1)

            # pick i
            sol.append(nums[i])
            backtrack(i)
            sol.pop()
        
        backtrack(0)   
        return res
            
            
        