# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# left -> root -> right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # base case
        if not root:
            return []
        
        # traversal
        left_sub = self.inorderTraversal(root.left)
        right_sub = self.inorderTraversal(root.right)

        return left_sub + [root.val] + right_sub
        