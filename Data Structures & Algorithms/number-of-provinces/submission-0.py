class DSU:
    def __init__(self, n) -> None:
        # +1?
        self.parents = list(range(n))
        self.rank = [1] * n
        self.provinces = n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.provinces -= 1
        if self.rank[px] > self.rank[py]:
            self.rank[px] += self.rank[py]
            self.parents[py] = px
        else:
            self.rank[py] += self.rank[px]
            self.parents[px] = py

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)

        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    dsu.union(r, c)

        return dsu.provinces
