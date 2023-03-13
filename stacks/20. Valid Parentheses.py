# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        par = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for p in s:
            if p in par:
                stack.append(p)
            else:
                if not stack or p != par[stack.pop()]:
                    return False
        return not stack
