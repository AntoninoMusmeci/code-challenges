# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root):
        prev = -100000
        min_dist = 1000000
        def dfs(root):
            nonlocal min_dist
            nonlocal prev
            if root == None:
                return
            dfs(root.left)
            min_dist = min(min_dist, root.val - prev)
            prev = root.val
            dfs(root.right)
        dfs(root)
        return min_dist