#https://leetcode.com/problems/generate-parentheses/description/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []
        def rec(stack = [], left = 0, right = 0):
            if len(stack) == n * 2:
                result.append("".join(stack))
                return
            if left < n:
                stack.append("(")
                rec(stack,left+1,right)
                stack.pop()
            if right < left: # the number of close ) should be less or equal the the number of open (
                stack.append(")")
                rec(stack,left,right+1)
                stack.pop()
        rec()
        return result