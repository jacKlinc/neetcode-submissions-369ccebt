class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [1] * n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                rank[p2] += rank[p1]
                parents[p2] = p1
            else:
                rank[p1] += rank[p2]
                parents[p1] = p2

            return True

        cnt = n
        for n1, n2 in edges:
            if union(n1, n2):
                cnt -= 1

        return cnt
