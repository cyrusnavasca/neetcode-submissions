# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case(s)
        if not subRoot: # exit when done evaluating subtree
            return True
        if not root:
            return False

        # check if current part of main tree matches subtree
        if self.isSameTree(root, subRoot):
            return True
        
        # traverse main tree, if subtree i
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case(s)
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        # if both left subtree and right subtrees are the same, then we are good
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
            
        
        