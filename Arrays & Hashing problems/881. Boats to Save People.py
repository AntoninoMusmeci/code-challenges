#https://leetcode.com/problems/boats-to-save-people/description/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        current_weight = 0
        total_boats = 0
        people.sort()

        l = 0
        r = len(people) - 1
        while l <= r:
            current_weight = people[l]
            while l<r and current_weight + people[r] > limit:
                total_boats += 1
                r -= 1
            total_boats += 1
            r-= 1
            l += 1
        return total_boats