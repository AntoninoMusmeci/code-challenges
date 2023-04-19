#https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node, dir, path_len):

            if node:
                nonlocal result
                result = max(result, path_len)
                if dir:
                    dfs(node.left, False, path_len + 1)
                    dfs(node.right, True, 1)
                else:
                    dfs(node.left, False, 1)
                    dfs(node.right, True, path_len + 1)

        dfs(root, False, 0)
        dfs(root, True, 0)
        return result
