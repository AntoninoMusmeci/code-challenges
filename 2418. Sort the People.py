# https://leetcode.com/problems/sort-the-people/description/
class Solution:
    def sortPeople(self, names, heights):
        return [x[1] for x in sorted(zip(heights, names),  reverse=True)]
