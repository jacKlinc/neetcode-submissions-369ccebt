class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False

            if rank[px] > rank[py]:
                rank[px] += rank[py]
                parents[py] = px
            else:
                rank[py] += rank[px]
                parents[px] = py

            return True

        cnt = n
        for n1, n2 in edges:
            if union(n1, n2):
                cnt -= 1

        return cnt
