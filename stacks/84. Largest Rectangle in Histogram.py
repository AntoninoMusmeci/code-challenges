#https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i,heights[i]))
                continue
            pos = 0
            while stack and heights[i] < stack[-1][1]:
                pos,h = stack.pop()
                max_area = max(max_area, h * (i - pos))
            stack.append((pos,heights[i]))
        return  max_area