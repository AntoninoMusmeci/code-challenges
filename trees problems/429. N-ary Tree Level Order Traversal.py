"""
https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution:
    def levelOrder(self, root: 'Node'):
        if root is None:
            return []
        queue = collections.deque([root])
        result = []

        while queue:
            level_len = len(queue)
            level = []
            while level_len > 0:
                level_len -= 1
                current_node = queue.popleft()
                level.append(current_node.val)
                for node in current_node.children:
                    queue.append(node)
            result.append(level)

        return result
