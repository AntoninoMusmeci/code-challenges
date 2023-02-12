from collections import defaultdict
from math import ceil
class Solution:
    fuel = 0
    def minimumFuelCost(self, roads, seats):
        #create a reppresentation of the graph (adjacency list )
       
        graph = defaultdict(list)
        for n1,n2 in roads:
            graph[n1].append(n2)
            graph[n2].append(n1)
        def dfs(node,par):
            representative = 1
            for neighbours in graph[node]:
                if neighbours != par:
                   representative += dfs(neighbours, node)
            current_fuel = ceil(representative/seats)
            if node != 0:
                self.fuel += current_fuel
            return representative
      
        dfs(0,None)
        
        return self.fuel