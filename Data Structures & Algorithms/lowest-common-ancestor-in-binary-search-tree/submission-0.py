# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
            # Case 1) One of the values is the root (of main tree or a subtree)
            if curr.val == p.val or curr.val == q.val:
                return curr

            # Case 3) Values are on opposite sides of the root
            if not ((p.val > curr.val and q.val > curr.val) or (p.val < curr.val and q.val < curr.val)):
                return curr

            # Case 2) Values are somewhere on the same side
            if p.val > curr.val:
                curr = curr.right

            else:
                curr = curr.left

        return curr

        