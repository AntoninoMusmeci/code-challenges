# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        left_to_right = True
        queue = collections.deque([root])
        result = []
        while queue:
            level_len = len(queue)
            current_level = []
            while level_len != 0:
                level_len -= 1
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                current_level = current_level[::-1]
            left_to_right = not left_to_right
            result.append(current_level)
        return result
