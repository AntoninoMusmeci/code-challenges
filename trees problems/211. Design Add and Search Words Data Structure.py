#https://leetcode.com/problems/design-add-and-search-words-data-structure/
class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        trie = self.trie
        for c in word: 
            if c not in trie:
                trie[c] ={}
            trie = trie[c]
        trie['*'] = {}

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def rec(i,word,trie):
            if i == len(word) : 
                return '*' in trie
            if word[i] not in trie and word[i] != '.':
                return False
            if word[i] == '.':
                for c in trie.values():
                    if rec(i+1, word,c):
                        return True
                return False
            else:
                return rec(i+1,word,trie[word[i]])
        return rec(0,word,self.trie)