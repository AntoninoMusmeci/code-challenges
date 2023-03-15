#https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        none_found = False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node == None:
                none_found = True
            else:
                if none_found:
                    return False
                queue.append(node.left if node.left else None)
                queue.append(node.right if node.right else None)
        return True