# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case(s)
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        # if we find a match, check if the trees match
        if root.val == subRoot.val:
            if self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right):
                return True
            else: 
                return False
        else:
            # if we havent matched yet, just keep traversing main tree
            return self.isSubtree(root.left, subRoot)
            return self.isSubtree(root.right, subRoot)
            
        
        