import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function to help recursively update lower/upper
        def isValid(node: Optional[TreeNode], lower=None, upper=None) -> bool:
            # base case
            if not node:
                return True
            
            # recursive step
            if not (node.val > lower and node.val < upper):
                return False
            
            return (isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper))
        
        return isValid(root, -math.inf, math.inf)
            

            
            

        