#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a,b: b + a,'-':lambda a,b: b - a,'/': lambda a,b: int(b/a),'*': lambda a,b: b * a}

        for t in tokens:
            if t in operations:
                x = operations[t]
                stack.append(x(stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack[-1]
