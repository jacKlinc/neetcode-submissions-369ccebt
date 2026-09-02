class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
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

        cnt = n
        for n1, n2 in edges:
            if union(n1, n2):
                cnt -= 1

        return cnt
