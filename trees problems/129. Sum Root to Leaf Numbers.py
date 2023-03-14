#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
       def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tot = 0
        def dfs(r,n):
            if not r.left and not r.right:
                nonlocal tot
                tot += int(n)
                return
            if r.left:
                dfs(r.left, n+str(r.left.val))
            if r.right:
                dfs(r.right, n + str(r.right.val))
        dfs(root, str(root.val))
        return tot 