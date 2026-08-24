# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res, sublist = [], []

        while queue:
            node = queue.popleft()
            sublist.append(node.val)
            if not queue:
                res.append(sublist)
                sublist = []
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return res

        