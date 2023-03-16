# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def rec(l,r):
            if l >= r: 
                return None
            v = postorder.pop()
            root = TreeNode(v)
            i = index_map[v]
            root.right = rec(i + 1, r)
            root.left = rec(l,i)
            return root
        
        index_map= {n:i for i,n in enumerate(inorder)}
        return rec(0,len(inorder))