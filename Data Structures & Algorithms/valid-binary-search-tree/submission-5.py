# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # base case
        if not root:
            return True
        
        # processing + traversal
        if root.left and (root.left.val > root.val or root.left.val == root.val) :
            return False
        if root.right and (root.right.val < root.val or root.right.val == root.val):
            return False
        else:
            return True
    
        return (isValidBST(root.left) or isValidBST(root.right))

        