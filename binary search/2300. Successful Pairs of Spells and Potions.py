#https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse = True)
        pair = []
        m = len(potions)
        for s in spells:
            minimum_potion_strenght = math.ceil(success/s)
            l = 0
            r = m - 1
            while l <= r:
                mid = (l+r)//2
                if potions[mid] >= minimum_potion_strenght:
                    l = mid + 1
                if potions[mid] < minimum_potion_strenght:
                    r = mid - 1
            pair.append(l)
        return pair