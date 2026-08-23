# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # base case
        if not root:
            return []
        
        # traversal
        node = root
        left_subtree = self.preorderTraversal(root.left)
        right_subtree = self.preorderTraversal(root.right)

        return [node.val] + left_subtree + right_subtree
        