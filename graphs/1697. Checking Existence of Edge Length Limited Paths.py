
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
         disSet = UnionFind(n)
         n_queries = len(queries)
         answer = [False] * n_queries
         queries_with_index = [query+[i] for i,query in enumerate(queries)]
         queries_with_index.sort(key = lambda x: x[2]) #sort by limit
         edgeList.sort(key = lambda x: x[2]) #sort by weight
         
         i = 0
         for query in queries_with_index:
             
            while i < len(edgeList) and edgeList[i][2] < query[2]:
                disSet.union(edgeList[i][0], edgeList[i][1])
                i+=1
            answer[query[3]] = disSet.connected(query[0],query[1])
         return answer