#https://leetcode.com/problems/min-stack/description/
class MinStack:
    def __init__(self):
        self.minstack = []
        self.stack = []
    def push(self, val: int) -> None:
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
