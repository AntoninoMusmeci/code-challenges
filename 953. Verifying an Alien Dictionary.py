# https://leetcode.com/problems/verifying-an-alien-dictionary/description/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #create a mapping between the order list characters and the position O(26) because the length of order is 26
        mapping = {c:i for i,c in enumerate(order) }

        for i in range(1,len(words)):
            #iterate over each pair of words
            for j in range(len(words[i-1])):
                if j >= len(words[i]): #this take care of cases like [hello, hell] 
                    return False
                if mapping[words[i-1][j]] < mapping[words[i][j]]:
                    break
                if mapping[words[i-1][j]] > mapping[words[i][j]]:
                    return False
        #if reach this line the words are sorted    
        return True  