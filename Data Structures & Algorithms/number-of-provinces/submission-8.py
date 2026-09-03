class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = list(range(n := len(isConnected)))
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] > rank[py]:
                rank[px] += rank[py]
                parents[py] = x
            else:
                rank[py] += rank[px]
                parents[px] = y

            return True

        global provinces
        provinces = n
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    if union(r, c):
                        provinces -= 1

        return provinces
