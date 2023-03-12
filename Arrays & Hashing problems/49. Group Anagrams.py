#https://leetcode.com/problems/group-anagrams/editorial/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        table = {}
        result = []
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c)-ord('a')] += 1
            word = tuple(word)
            table[word] = table.get(word,[]) + [s]
        for lists in table.values():
            result.append(lists)
        return result