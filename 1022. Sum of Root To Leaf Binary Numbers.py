#https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root,num):
            result = 0
            num = num << 1 | int(root.val)
            if not root.left and not root.right:
                return num
            if root.left: result += dfs(root.left, num)
            if root.right: result += dfs(root.right, num)
            return result
    
        return dfs(root,0)