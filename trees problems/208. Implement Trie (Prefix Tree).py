#https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t["*"] = "*"
        

    def search(self, word):
        trie = self.trie
        for char in word:
            if char in trie:
                trie = trie[char]
            else:
                return False
        return '*' in trie
        

    def startsWith(self, prefix):
        trie = self.trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return False
        return True