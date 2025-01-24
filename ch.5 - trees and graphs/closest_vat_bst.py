# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def dfs(node):
            if not node:
                return
            
            nonlocal minimum, res
            if abs(node.val - target) < minimum:
                minimum = abs(node.val - target)
                res = node.val
            if node.val < target:
                dfs(node.right)
            else:
                dfs(node.left)
        minimum = float('inf')
        res = 0
        dfs(root)
        return res
        