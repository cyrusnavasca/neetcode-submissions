# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case(s)
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # recursively track is left subtrees are same, then right subtrees
        return self.isSameTree(p.left, q.left)
        return self.isSameTree(p.right, q.right)

        return True

        









        