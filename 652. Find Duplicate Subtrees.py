# https://leetcode.com/problems/find-duplicate-subtrees/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        result = []
        subtrees = {}

        def dfs(root):
            s = str(root.val)
            if root.left:
                s += "l" + dfs(root.left)
            if root.right:
                s += "r" + dfs(root.right)
            subtrees[s] = subtrees.get(s, 0) + 1
            if subtrees[s] == 2:
                result.append(root)
            return s + '-'
        dfs(root)
        print(subtrees)
        return result
