# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pre order traver
        if not root:
            return True
        if root.right.val < root.val or root.left.val > root.val:
            return False
        else:
            return True

        return (isValidBST(root.left) or isValidBST(root.right))

        