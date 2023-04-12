#https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for p in path.split("/"):
            if p == ".." and stack:
                stack.pop()
            if p and p != "." and p != "..":
                stack.append(p)
        return "/" + "/".join(stack)