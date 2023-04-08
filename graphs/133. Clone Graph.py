#https://leetcode.com/problems/clone-graph/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        nodeMap = {}

        def dfs(node):
            if not node:
                return node
            node_copy = Node(val = node.val, neighbors = [] )
            nodeMap[node.val] = node_copy
            for nei in node.neighbors:
                if nei.val in nodeMap:
                    node_copy.neighbors.append(nodeMap[nei.val])
                else:
                    node_copy.neighbors.append(dfs(nei))
            return node_copy
        return dfs(node)
