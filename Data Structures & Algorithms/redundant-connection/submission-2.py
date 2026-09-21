class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        edges that we cannot take away are
        edges that go to vertices with no children

        could go through each edge and try
        removing each 
        if graph gets split into two components:
            false, not connected
        start from the back and go forward
        if graph stays as one:
            traverse from each V in the removed edge
        if V can reach all v-1
            good
root    1 1 1 1 5 
        1 2 3 4 5
        if find(3) and find(4) already have the same root
        this would be a cycle so can remove this edge
        so build graph as union find

        edge cases:

none since n = edges and starts connected guaranteed one cycle
        '''
        n = len(edges)
        uf = UnionFind(n)
        for st,ed in (edges):
            if (uf.find(st) != uf.find(ed)):
                uf.union(st,ed)
            else:
                return [st,ed]
        return [0,0]
class UnionFind:
    def __init__(self, size):
        self.root = [ i for i in range(size+1)]
        self.rank = [1] * (size+1)
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if (rx != ry):
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
                self.rank[rx] += self.rank[ry]
            elif self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
                self.rank[ry] += self.rank[rx] 
            else:
                # equal case
                self.root[ry] = rx
                self.rank[rx] += self.rank[rx]
