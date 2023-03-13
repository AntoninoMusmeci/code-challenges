#https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [(temperatures[0],0)]
        result = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                t,pos = stack.pop()
                result[pos] = i - pos
            stack.append((temperatures[i],i))
        return result