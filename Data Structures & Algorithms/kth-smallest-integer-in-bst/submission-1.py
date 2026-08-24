# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-Order Traversal
        def inorder(node: Optional[TreeNode]) -> List:
            arr = []
            # base case
            if not node:
                return []
            
            left_subtree = inorder(node.left)
            right_subtree = inorder(node.right)

            return left_subtree + [node.val] + right_subtree
        
        arr = inorder(root)
        print(arr)
        return arr[k-1]