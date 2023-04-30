#https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
class UnionFind:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.rank = [1] * N
        self.components = N
    def find(self, p: int) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: 
            prt, qrt = qrt, prt 
        self.parent[prt] = qrt 
        self.rank[qrt] += self.rank[prt] 
        self.components -= 1
        return True
    def connected(self,a,b):
        return self.find(a) == self.find(b)
    def allConnected(self):
        return self.components == 1
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        a_graph = UnionFind(n)
        b_graph = UnionFind(n)
        edges.sort(key = lambda x: x[0], reverse= True)
        result = 0

        for edge in edges:
            a = edge[1] - 1
            b = edge[2] - 1
            if edge[0] == 1:
                if not a_graph.connected(b, a):
                    a_graph.union(b,a)
                else: result += 1
            if edge[0] == 2:
                if not b_graph.connected(b, a):
                    b_graph.union(b,a)
                else: result += 1
            if edge[0] == 3:
                if not a_graph.connected(b, a) or not b_graph.connected(b, a):
                    a_graph.union(b,a)
                    b_graph.union(b,a)
                else: result += 1
        return result if (a_graph.allConnected() and b_graph.allConnected()) else -1