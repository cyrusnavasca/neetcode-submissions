# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # base case(s)
        if not root:
            return root

        # 1) we hit one of them
        if p.val == root.val or q.val == root.val:
            return root
        
        # 2) on OPPOSITE SIDES
        if (p.val > root.val and q.val < root.val) or (p.val < root.val and q.val > root.val):
            return root

        # traversal (same side)
        return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)






        